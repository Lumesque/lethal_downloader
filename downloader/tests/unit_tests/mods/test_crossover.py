" Makes sure that when a text file is provided, there will be no duplication of adding to mod list "

import pytest
from mods.utils import get_mod_list, ModList

@pytest.fixture
def txt_fd():
    return io.StringIO("""E_Moons
Aquarium""")

@pytest.fixture
def mock_mod_list():
    # this will be a json with information about each mod, just add on
    return ModList({"E_Moons": {"version": "latest", "strict": False, "url": ""}})
