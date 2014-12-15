# Template for local_settings.py

EMAIL_USE_TLS = True
EMAIL_HOST = 'emailhost.com'
EMAIL_PORT = 'XXX'
EMAIL_HOST_USER = 'email@domain.com'
EMAIL_HOST_PASSWORD = 'password'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Your Name', 'email@domain.com'),
)

MANAGERS = ADMINS

STATIC_ROOT = '/var/www/static/'

STATIC_URL = 'http://www.yoursite.com/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hofuHistoric',
        'USER': 'db user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

SECRET_KEY = 'secret key'