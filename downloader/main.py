from .mods.Mods import Mod
from .utils import update_mods
from pathlib import Path
import json
import logging
from typing import NamedTuple, List
from .web_drivers.web import CommonDriver
from collections import deque

logger = logging.getLogger('main')

class Settings(NamedTuple):
    driver: CommonDriver
    mods: List[Mod]
    strict: bool = False

def main(settings: "Settings", force_all_latest=False):
    driver = settings.driver
    mods = settings.mods
    logger.info("Starting version control, looking through all mods")
    with driver as driver:
        mods = update_mods(driver, mods)
        for mod in mods:
            if force_all_latest:
                mod.version = "latest"
            driver.download(mod)
        input("Press any button to continue")
    print("Finished")

if __name__ == "__main__":
    settings = Settings(
            driver = CommonDriver(web_browser="chrome"),
            mods = [
                Mod(name="E_Gypt_Moon", url="https://thunderstore.io/c/lethal-company/p/KayNetsua/E_Gypt_Moon/"), 
                Mod(name="MoonOfTheDay") 
                ]
        )
    main(settings)
