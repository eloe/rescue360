from __future__ import absolute_import
from .base import *

# Configure these however you like for local development.
# Don't forget to configure a database!

DEBUG=True
TEMPLATE_DEBUG=DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'crazyweber_res2',      # Or path to database file if using sqlite3.
        'USER': 'crazyweber_res2',      # Not used with sqlite3.
        'PASSWORD': '6jZ26jqborw8AZ',          # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}