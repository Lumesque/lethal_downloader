from .Mods import Mod
from attrs import define, field
from typing import List


class ModContainer(list):

    def to_json(self):
        out = {}
        dicts = [mod.to_dict() for mod in self]
        for _dict in dicts:
            out[_dict.pop("name")] = _dict
        return out
