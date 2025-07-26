from .base import *

INTERNAL_IPS = ['127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT', '9200')

ELASTICSEARCH_DSL={
    'default': {
        'hosts': f'http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}'
    }
}

INSTALLED_APPS += ["debug_toolbar", 'silk']

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'silk.middleware.SilkyMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'