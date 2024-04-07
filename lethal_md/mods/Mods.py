from attrs import define, field, asdict
from pathlib import Path
from typing import Union, Optional

@define
class Version:
    version: str = field(default="latest", eq=False)  
    major: int = field(init=False, converter = int)
    minor: int = field(init=False, converter = int)   
    patch: int = field(init=False, converter = int)
    extras: list[int] = field(init=False, eq=False)

    def __attrs_post_init__(self):
        if self.version == "latest":
            nums = [999 for _ in range(3)]
        else:
            nums = self.version.split(".")
        self.major, self.minor, self.patch, *self.extras = nums
         
    def __lt__(self, other):
        if self.major < other.major:
            return True
        elif self.minor < other.minor:
            return True
        elif self.patch < other.patch:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.major > other.major:
            return True
        elif self.minor > other.minor:
            return True
        elif self.patch > other.patch:
            return True
        else:
            return False

    def __str__(self):
        return self.version

@define
class Mod:
    name: str
    version: str = field(default="latest", eq=False, converter=Version)
    _strict: bool = field(default=False, eq=False, repr=False, alias='_strict')
    # None is the value if we don't know the value, allow it in the setter
    url: Optional[Union[str, Path]] = field(
            default=None, 
            eq=False,
            converter = lambda x: Path(x) if x is not None else None
            )

    def to_dict(self):
        out = asdict(self)
        out['version'] = out['version']['version']
        out['url'] = str(out['url'])
        return out
