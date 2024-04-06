from pathlib import Path
from .Mods import Mod
from attrs import define, field
from typing import List, Union
import json

import os


class ModContainer(list):

    def to_json(self):
        out = {}
        dicts = [mod.to_dict() for mod in self]
        for _dict in dicts:
            out[_dict.pop("name")] = _dict
        return out

    @classmethod
    def from_json(cls, json) -> List[Mod]:
        out = cls()
        for name, mod in json.items():
            out.append(Mod(name, **mod))
        return out

