from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mmvg!6v5)&@7pw=x$7e-0)u2$5o#al_)2)h!i2m-$m)u&cq^#x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_TOOLBAR = True

INTERNAL_IPS=['127.0.0.1']
ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
] + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'PROJ',
#         'USER': 'django',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
