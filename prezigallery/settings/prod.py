import os
import dj_database_url

from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

DEBUG = False

ALLOWED_HOSTS = ['teglanna-prezi.herokuapp.com']

# Update database configuration with $DATABASE_URL. (used from Heroku docs)
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
