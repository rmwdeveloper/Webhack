from base import *

try:
    from local_settings import *
except ImportError:
    raise ImportError('Add settings/local_settings.py to hold secret info ')
