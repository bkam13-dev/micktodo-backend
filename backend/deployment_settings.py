import os
import dj_database_url
from .settings import *
from decouple import config, Csv 


RENDER_HOST = os.environ.get('RENDER_EXTERNAL_HOSTNAME') 
DATABASE_URL = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY') # Utiliser os.environ.get

DEBUG = False 

ALLOWED_HOSTS = [RENDER_HOST] if RENDER_HOST else [] 

if RENDER_HOST:
    CSRF_TRUSTED_ORIGINS = ['https://' + RENDER_HOST]
    CSRF_TRUSTED_ORIGINS.append('https://micktodo-frontend.vercel.app')
else:
    CSRF_TRUSTED_ORIGINS = []

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True



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


cors_origins_raw = os.environ.get('CORS_ALLOWED_ORIGINS', '')
CORS_ALLOWED_ORIGINS = cors_origins_raw.split(',') if cors_origins_raw else []


STORAGES = {
    "default":{
        "BACKEND" : "django.core.files.storage.FileSystemStorage"
    },
    "staticfiles":{
        "BACKEND" : "whitenoise.storage.CompressedManifestStaticFilesStorage" 
    },
}

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=True 
    )
}