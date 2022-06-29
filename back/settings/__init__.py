"""Settings for django project."""

from os import environ

from dotenv import load_dotenv

from .celery import app as celery_app

__all__ = ["celery_app"]

load_dotenv()

stage = environ.get("STAGE")

if not stage:
    raise ValueError("STAGE is not set")

if stage == "PRODUCTION":
    from settings.production import *
elif stage == "CI":
    from settings.test import *
else:
    from settings.dev import *
