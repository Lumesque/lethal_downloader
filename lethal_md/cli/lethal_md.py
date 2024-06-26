import argparse
import subprocess
import sys
from pathlib import Path


def return_action(here):
    class ActionParser(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            values = values.replace('.', '/')
            values += '.py'
            setattr(namespace, self.dest, Path(here, values))
    return ActionParser

def main() -> int:
    here = Path(__file__).parent
    options =[
        x.with_suffix('').parts[-2:]
        for x in here.glob("**/*") if "lethal_md" not in x.name and x.parts[-2] != "cli"]
    options = [".".join(x) for x in options if not x[0].startswith("_") and not x[1].startswith("_")]

    parser = argparse.ArgumentParser(
            description = f"Download mods for lethal company, and version control them using jsons",
    )
    parser.add_argument(
        'script',
        choices=options,
        action=return_action(here)
    )
    args, *extras = parser.parse_known_args(sys.argv[1:2])
    return subprocess.run(["python", args.script, *sys.argv[2:]])



if __name__ == "__main__":
    main()
