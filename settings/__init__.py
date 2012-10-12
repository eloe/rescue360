from __future__ import absolute_import
import os

if 'EPIO' in os.environ:
    from .epio import *
elif 'crazyweber' ==  os.environ['USER']:
    from .webfaction import *
elif 'eloe' == os.environ['USER']:
    from .eric import *
else:
    try:
        from .rick import *
    except ImportError:
        from .base import *