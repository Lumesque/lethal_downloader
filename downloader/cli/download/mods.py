import json
import argparse
from ...web_drivers.web import CommonDriver 
from ...mods.containers import ModContainer
from pathlib import Path


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
    args = parser.parse_args()
    with args.json.open(mode="r") as f:
        _dict = json.load(f)
    mods = ModContainer.from_json(_dict)
    with CommonDriver(web_browser=args.driver) as driver:
        for mod in mods:
            driver.download(mod)
        input("Press any button to continue")


if __name__ == "__main__":
    main()
