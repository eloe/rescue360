from __future__ import absolute_import
import os

if 'EPIO' in os.environ:
    from .epio import *
elif 'crazyweber' ==  os.environ['USER']:
    from .webfaction import *
else:
    try:
        from .local import *
    except ImportError:
        from .base import *