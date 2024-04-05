from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dataclasses import dataclass, InitVar, field
from collections import namedtuple
from typing import Any
from contextlib import suppress
from ..mods.Mods import Mod
from ..exceptions import BrowserNotFound
import time
import re

DEFAULT_SEARCH = "https://thunderstore.io/c/lethal-company/"
LethalDownloadDiv = namedtuple("LethalDownloadDiv", ["text", "img"])

@dataclass
class CommonDriver:
    web_browser: str
    drive_cls: Any = None
    driver: Any = field(init=False, repr=False, default=None)

    def __post_init__(self):
        if self.drive_cls is None:
            try:
                self.drive_cls = eval(f"webdriver.{self.web_browser.title()}")
            except AttributeError as e:
                raise BrowserNotFound(f"{self.web_browser.title()} not found, not a valid browser") from e

    def start(self):
        if not self.started:
            self.driver = self.drive_cls()

    @property
    def started(self):
        return False if self.driver == None else True

    def get(self, link):
        self.driver.get(str(link))

    def get_clickable_images_and_text(self):
        text = self.driver.find_elements(By.TAG_NAME, "h5")
        imgs = [x for x in self.driver.find_elements(By.CLASS_NAME, "w-100")
                if x.tag_name == "img"]
        if len(text) != len(imgs):
            raise ValueError("Could not align text with clickable images")
        elif not text and not imgs:
            raise ValueError("Expected text and images, not populated")
        return [LethalDownloadDiv(text=txt.text, img=img) for txt, img in zip(text, imgs)]

    def search(self, mod):
        self.get(DEFAULT_SEARCH)
        search_box = self.driver.find_element(By.TAG_NAME, "input")
        search_box.send_keys(mod)
        search_box.submit()

    # Uses custom class
    def download(self, mod):
        self.get(mod.url)
        if str(mod.version) == 'latest':
            [x for x in self.driver.find_elements(By.XPATH, "//a[@type='button']")
             if x.text == 'Manual Download'][0].click()
        else:
            string = f'{mod.version}'
            _version_index = 1   
            _download_index = 3
            [versions_page] = [x for x in self.driver.find_elements(By.CLASS_NAME, "nav-link")
                               if x.text == "Versions"]
            versions_page.click()
            [table] = [x for x in self.driver.find_elements(By.XPATH, "//table")]
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:

                data = row.find_elements(By.TAG_NAME, "td")
                if not data:
                    continue
                elif data[1].text == string:
                    data[_download_index].find_elements(By.TAG_NAME, "a")[0].click()
                    break

    def update(self, mod, force=False, force_latest_dependencies=False):
        if mod.url is None or force is True:
            self.search(mod.name.replace(' ', '_'))
            download_divs = self.get_clickable_images_and_text()
            conv_str = lambda x: x if mod.strict else x.lower()
            if len(download_divs) == 1:
                wanted_mod = download_divs[0]
            else:
                [wanted_mod] = [x for x in download_divs
                                if conv_str(x.text) == conv_str(mod.name)]
            wanted_mod.img.click()
            mod.url = self.driver.current_url
        else:
            self.get(mod.url)
        values_to_return = [mod]
        with suppress(ValueError):
            values_to_return.extend(self.current_dependencies(force_latest_dependencies))
        return values_to_return

    def current_dependencies(self, force_latest=False):
        get_version = lambda x: x.replace('Preferred version: ','') \
                      if not force_latest else "latest"
        [h4] = [x for x in self.driver.find_elements(By.XPATH, '//h4')
                if 'requires the following mods to function' in x.text.lower()]
        named_text = h4.find_element(By.XPATH, '..')
        named_text = named_text.find_element(By.XPATH, '..')
        packages = named_text.text.split('\n')[1:]
        hrefs = self.driver.find_elements(By.XPATH, "//a")
        dependencies = [x for x in hrefs if x.text in packages[::3]]
        returns = []
        for dependency, version in zip(dependencies, packages[2::3]):
            name = dependency.text.split('-')[1].replace('_', ' ')
            returns.append(
                           Mod(name=name,
                               version=get_version(version),
                               url=dependency.get_attribute("href"))
                           )
        return returns

    def close(self):
        self.driver.close()
        self.driver = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
