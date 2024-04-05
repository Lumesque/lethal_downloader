from .mods.Mods import Mod
from .mods.containers import ModContainer

def main(force=False, force_all_latest=False):
    ok, mods = ModContainer.from_cache(cachedir = os.environ.get('MODS_CACHE_DIR', os.path.expanduser('~/.mods_cache')))
    if ok is not True:
        mods = ModContainer()
