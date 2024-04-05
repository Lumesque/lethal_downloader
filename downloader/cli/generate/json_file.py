import argparse
import json
from pathlib import Path
from ...mods.Mods import Mod
from ...mods.containers import ModContainer
from ...web_drivers.web import CommonDriver
from ...utils import update_mods

def main():
    parser = argparse.ArgumentParser(
            description = 'Generate JSON file for mod packs'
            )
    parser.add_argument(
        'file',
        type = Path,
        help="File with list of mod names separated by new line"
    )
    parser.add_argument(
            '-u',
            '--update',
            action='store_true',
            help="Update mod url paths and put them into json, find dependencies, and change version dependencies if applicable"
            )
    parser.add_argument(
            '-d',
            '--driver',
            help="Web driver to use",
            default="Chrome"
            )
    args = parser.parse_args()
    container = ModContainer()

    with args.file.open(mode="r") as f:
        for line in f:
            container.append(
                    Mod(line.strip())
                    )
    if args.update:
        with CommonDriver(web_browser=args.driver) as driver:
            container = update_mods(driver, container, get_latest=True)

    with args.file.with_suffix('.json').open(mode="w") as f:
        json.dump(container.to_json(), f,indent=4)

if __name__ == "__main__":
    main()
