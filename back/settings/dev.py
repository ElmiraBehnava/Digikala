"""Dev settings for django project."""

from fnmatch import fnmatch
from os.path import join, normpath
from socket import gethostbyname, gethostname

from settings.common import *

## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = DEBUG
## END DEBUG CONFIGURATION

## EMAIL CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
## END EMAIL CONFIGURATION

## CACHE CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}
## END CACHE CONFIGURATION

## TOOLBAR CONFIGURATION
INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
## END TOOLBAR CONFIGURATION
