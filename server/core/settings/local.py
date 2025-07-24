from .base import *

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
ALLOWED_HOSTS = ALLOWED_HOSTS.split(',') if ALLOWED_HOSTS else ['localhost', '127.0.0.1', '0.0.0.0']

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