import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR
from decouple import config, Csv


RENDER_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
DATABASE_URL = os.environ.get('DATABASE_URL')



ALLOWED_HOSTS = RENDER_HOSTNAME
CSRF_TRUSTED_ORIGINS = ['https://'+ RENDER_HOSTNAME]

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]  


CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS')

STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.FileSystemStorage"
    },
    "staticfiles":{
        "BACKEND" : "whitenoise.storage.CompressedStaticFilesStorage"
    },
}


DATABASES = {
    "default": dj_database_url.config(
        default=os.environ['DATABASE_URL'],
        conn_max_age=600,
        ssl_require=True
    )
}


# SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT')
# SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE')
# CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE')