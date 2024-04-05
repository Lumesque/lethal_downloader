from collections import deque

def update_mods(installer, mods, get_latest = False, ignore_errors = True):
    find_urls = deque(mods)
    while find_urls:
        current_mod = find_urls.popleft()
        try:
            extra_mods = installer.update(current_mod, get_latest=get_latest)
            for mod in extra_mods:
                if mod in mods and mod.url is not None:
                    [mod_to_update] = [x for x in mods if x == mod]
                    if mod_to_update.url is None:
                        mod_to_update.url = mod.url
                    elif mod_to_update.url != mod.url:
                        print("Got conflicting results for mod", mod.url, mod_to_update.url)
                    if str(mod_to_update.version) != 'latest':
                        if mod.version > mod_to_update.version:
                            mod_to_update.version = str(mod.version)
                else:
                    mods.append(mod)
                    find_urls.append(mod)
        except Exception as e:
            if not ignore_errors:
                raise e
            else:
                print("Error while updating mod", current_mod, e)
    return mods

