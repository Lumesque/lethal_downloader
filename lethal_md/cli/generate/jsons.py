import argparse
import json
import os
import sys

path = os.path.realpath(os.path.dirname(__file__) + '/../../..')
sys.path.insert(0, path)    
from pathlib import Path

from lethal_md.mods.containers import ModContainer
from lethal_md.mods.Mods import Mod
from lethal_md.navigators.web import CommonDriver
from lethal_md.utils import update_mods


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
            help="When updating mod paths and dependencies, change version dependencies or versions of latest to actual verison numbers if applicable"
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
    with CommonDriver(web_browser=args.driver) as driver:
        container = update_mods(driver, container, args.update)

    with args.file.with_suffix('.json').open(mode="w") as f:
        json.dump(container.to_json(), f,indent=4)
    print("Wrote to ", args.file.with_suffix('.json'))

if __name__ == "__main__":
    main()
