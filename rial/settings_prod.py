DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'rial',
        'PASSWORD': 'qwe224169',
        'HOST': 'localhost',
        'PORT': '',
    }
}