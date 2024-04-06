import importlib
try: 
    __version__ = importlib.import_module('_version').__version__
except: 
    __version__ = 'unknown'
