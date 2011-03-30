import os
from decimal import Decimal

PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
LOCAL_DEV = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Adam Miskiewicz', 'adam.skevy@mac.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',                 # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'radiolocator', # Or path to database file if using sqlite3.
        'USER': 'gis',                                             # Not used with sqlite3.
        'PASSWORD': 'Ada2kath',                                         # Not used with sqlite3.
        'HOST': '',                                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                             # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
MEDIA_URL = '/media/'
MEDIA_URLS = ()

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/')
STATIC_URL = '/static/'
STATIC_URLS = ()

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '5oobt_px9g877%&*#m7fgnq_(igh4!t&s&u%r^gn+g36%!x2id2bbivov'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'radio_locator.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.gis',
    
    'radio_locator',
    'radio_locator.locator',
        
    'django_extensions',
    'south',
)

# CACHE_BACKEND = 'locmem://'

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

try:
    from j3utils.contrib.config import load_yaml
    load_yaml("/etc/radio-locator/radio-locator.yml", globals())
except:
    pass
    
try:
    from local_settings import *
except:
    pass