import argparse
import json
import os
import sys

path = os.path.realpath(os.path.dirname(__file__) + '/../../..')
sys.path.insert(0, path)    
from pathlib import Path

from lethal_md.mods.containers import ModContainer
from lethal_md.navigators.web import CommonDriver
from lethal_md.utils import download_mods


def main(): 
    parser = argparse.ArgumentParser(
            description = "Download mods from Thunderstore using JSON"
            )
    parser.add_argument(
        'json',
        type = Path,
        help="Generated JSON with mods"
    )
    parser.add_argument(
            '-d',
            '--driver',
            help="Web driver to use",
            default="Chrome"
            )
    parser.add_argument(
            '-f',
            '--force-latest',
            dest = "force",
            help="Force latest version download",
            action='store_true'
            )
    args = parser.parse_args()
    with args.json.open(mode="r") as f:
        _dict = json.load(f)
    mods = ModContainer.from_json(_dict)
    with CommonDriver(web_browser=args.driver) as driver:
        download_mods(driver, mods, args.force, ignore_errors = True)
        input("Press any button to continue")


if __name__ == "__main__":
    main()
