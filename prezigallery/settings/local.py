import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = 'http://localhost:8888/media/'
