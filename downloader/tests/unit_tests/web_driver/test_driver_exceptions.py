from driver.exceptions import (
        BrowserNotFound
)
import pytest
from driver.utils import find_driver

@pytest.fixture()
def driver():
    return WebDriver()

def test_browser_not_found(driver):
    with pytest.raises(BrowserNotFound):
        find_driver('firefox')


