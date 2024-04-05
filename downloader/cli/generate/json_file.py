import argparse
import json
from pathlib import Path
from ...mods.Mods import Mod
from ...mods.containers import ModContainer

def main():
    parser = argparse.ArgumentParser(
            description = 'Generate JSON file for mod packs'
            )
    parser.add_argument(
        'file',
        type = Path,
        help="File with list of mod names separated by new line"
    )
    args = parser.parse_args()
    container = ModContainer()

    with args.file.open(mode="r") as f:
        for line in f:
            container.append(
                    Mod(line.strip())
                    )
    with args.file.with_suffix('.json').open(mode="w") as f:
        json.dump(container.to_json(), f,indent=4)

if __name__ == "__main__":
    main()
