from decouple import config, Csv
from pathlib import Path
import os
import dj_database_url # Importé pour le parsing de l'URL PostgreSQL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# =================================================================
# 1. DÉTECTION ET SÉCURITÉ (Lu par config() depuis l'environnement ou .env)
# =================================================================

# La clé secrète est lue depuis l'environnement (Render) ou le fichier .env (Local)
SECRET_KEY = config('SECRET_KEY')

# Le mode DEBUG est lu depuis l'environnement ou .env (doit être False en Prod)
DEBUG = config('DEBUG', default=False, cast=bool)

# Vérifie si la variable RENDER_EXTERNAL_HOSTNAME existe (c'est Render qui la donne)
IS_RENDER = os.environ.get('RENDER_EXTERNAL_HOSTNAME') is not None

# HÔTES AUTORISÉS (Gère la liste complète du .env et ajoute l'hôte Render)
# Lit toujours la liste du .env (qui contient localhost, 127.0.0.1, et le domaine Vercel)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

if IS_RENDER:
    # Production : Ajoute l'hôte Render à la liste déjà lue du .env
    RENDER_HOST = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_HOST and RENDER_HOST not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(RENDER_HOST)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'tasks',
    'authentification',
]

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

AUTH_USER_MODEL = "authentification.User"

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# =================================================================
# 2. BASE DE DONNÉES (Gestion de la priorité Prod/Dev)
# =================================================================

# Tente de récupérer l'URL de connexion complète (Production)
DATABASE_URL_FULL = config('DATABASE_URL', default=None)

if DATABASE_URL_FULL:
    # --- CONFIGURATION PRODUCTION (RENDER) ---
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL_FULL,
            conn_max_age=600, 
            ssl_require=True  # EXIGÉ en Production
        )
    }

else:
    # --- CONFIGURATION LOCALE (DEV) ---
    # Utilise les variables détaillées du .env pour la connexion locale PostgreSQL
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE'),
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =================================================================
# 3. CORS ET SÉCURITÉ HTTPS
# =================================================================

# CORS : Lit la liste formatée par virgules du .env
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='', cast=Csv())

# SÉCURITÉ HTTPS (Doit être True en Prod si vous avez un domaine personnalisé)
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=False, cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=False, cast=bool)
X_FRAME_OPTIONS = config('X_FRAME_OPTIONS', default='SAMEORIGIN')