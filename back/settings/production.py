"""Production settings for django project."""

from settings.common import *
from os import environ
from django.core.exceptions import ImproperlyConfigured

## PRODUCTION APPS CONFIGURATION
INSTALLED_APPS = ("corsheaders",) + INSTALLED_APPS + ("gunicorn",)
## PRODUCTION APPS CONFIGURATION

## EMAIL CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = get_env("EMAIL_HOST", optinal=True)
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD", optinal=True)
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER", optinal=True)
EMAIL_PORT = get_env("EMAIL_PORT", optinal=True)
EMAIL_SUBJECT_PREFIX = "[{}] ".format(SITE_NAME)
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
## END EMAIL CONFIGURATION

## MINIO CONFIGURATION
DEFAULT_FILE_STORAGE = get_env("DEFAULT_FILE_STORAGE", default='django.core.files.storage.FileSystemStorage')
STATICFILES_STORAGE = get_env("STATICFILES_STORAGE", default='django.contrib.staticfiles.storage.StaticFilesStorage')
MINIO_STORAGE_ENDPOINT = get_env("MINIO_STORAGE_ENDPOINT", optinal=True)
MINIO_STORAGE_ACCESS_KEY = get_env("MINIO_STORAGE_ACCESS_KEY", optinal=True)
MINIO_STORAGE_SECRET_KEY = get_env("MINIO_STORAGE_SECRET_KEY", optinal=True)
MINIO_STORAGE_MEDIA_BUCKET_NAME = get_env("MINIO_STORAGE_MEDIA_BUCKET_NAME", optinal=True)
MINIO_STORAGE_STATIC_BUCKET_NAME = get_env("MINIO_STORAGE_STATIC_BUCKET_NAME", optinal=True)
## END MINIO CONFIGURATION

######### CORSHEADERS CONFIGURATION
CSRF_TRUSTED_ORIGINS = get_env("CSRF_TRUSTED_ORIGINS", default="").split(",")
CSRF_COOKIE_DOMAIN = get_env("CSRF_COOKIE_DOMAIN", optinal=True)
CORS_ORIGIN_REGEX_WHITELIST = [r""]  # TODO fill this
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = r""  # TODO fill this
######### END CORSHEADERS CONFIGURATION
