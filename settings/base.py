from unipath import FSPath as Path
import datetime

PROJECT_DIR = Path(__file__).absolute().ancestor(2)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Eric Loes', 'eric@hardlycode.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
VERSION = '122711a'
USE_I18N = True
USE_L10N = True

IMAGE_MAX_RESOLUTION=(800,600)
IMAGE_THUMB_RESOLUTION=(140, 140)
IMAGE_THUMB_SQUARED=True
IMAGE_USE_S3=True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID='AKIAIHC3NLUDSD3KCUTQ'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME='rescue360'
AWS_S3_SECURE_URLS=False
now = datetime.datetime.now()
AWS_HEADERS = {
    'Expires': 'Thu, 15 %d %d 20:00:00 GMT' % (now.month+1, now.year),
    'Cache-Control': 'max-age=86400',
}

EMAIL_USE_TLS = True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='do-not-reply@hardlycode.com'
EMAIL_HOST_PASSWORD='g7zwDV5oHpAM'
EMAIL_PORT=587
EMAIL_RECIPIENTS=['sales@hardlycode.com']

TWITTER_USERNAME='hardlycode'

MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('core').child('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (

)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '1rm*90m8a%xz+$lasf134fg-s-e1w&@$^=2k7ba*i%pbc=xw0cgs'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#   'hardlycode.middleware.blowfish.BlowfishMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('core').child('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'epio_commands',
    'django.contrib.admin',
	'core',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}