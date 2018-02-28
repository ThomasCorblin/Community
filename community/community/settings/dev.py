from community.settings.base import *

#override default settings here


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'communitydb',
        'USER': 'admin',
        'PASSWORD': 'Pass123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_HOST= 'localhost'
EMAIL_PORT= '1025'

STATICFILES_DIRS = ['static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

try:
    from tutorial.settings.local import *
except:
    pass

