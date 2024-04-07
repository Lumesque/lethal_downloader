import importlib

try: 
    __version__ = importlib.import_module('._version', package=__package__).__version__
except: 
    __version__ = 'unknown'
