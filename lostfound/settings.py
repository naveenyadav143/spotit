from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-81ptsm8m5r!+q7g!jzwt-q7n*#pq2rd&w754&95b*6*#4km#e-'

DEBUG = False

ALLOWED_HOSTS = [
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# ---------------------------
# INSTALLED APPS
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'data',

    'cloudinary',
    'cloudinary_storage',
]

# ---------------------------
# MIDDLEWARE
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lostfound.urls'

# ---------------------------
# TEMPLATES
# ---------------------------
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

WSGI_APPLICATION = 'lostfound.wsgi.application'

# ---------------------------
# DATABASE
# ---------------------------
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL")
    )
}


# ---------------------------
# PASSWORD VALIDATION
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------
# INTERNATIONALIZATION
# ---------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------
# STATIC FILES
# ---------------------------
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------
# DRF
# ---------------------------
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# ============================================================
#                 CLOUDINARY CONFIG  (Django 5)
# ============================================================

# Option A: Using environment variable (recommended)
# CLOUDINARY_URL=cloudinary://<API_KEY>:<API_SECRET>@<CLOUD_NAME>
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

# Option B: Explicit manual keys
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dkd0uchyq",        # <--- CHANGE THIS
    "API_KEY": "227343851876187",              # <--- CHANGE THIS
    "API_SECRET": "qnpFLKJbER0OjVueeEEV1T9eeBM",        # <--- CHANGE THIS
}

# Django 5 storage system
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# (Optional) Public media URL, Cloudinary doesn't need MEDIA_ROOT
MEDIA_URL = "/media/"
