import environ
import os
import sys

from pathlib import Path

env = environ.FileAwareEnv(
    SECRET_KEY=(str, 'django-insecure-o*oim^p40)mkx$k$e5clx5fu53znjc2)6xgey0#7j4tfs%s4z$'),
    DEBUG=(bool, True),
    SQL_HOST=(str, 'localhost'),
    SQL_USER=(str, 'postgres'),
    SQL_PASSWORD=(str, 'postgres'),
)
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY').strip()

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', 'backend']

# Session lifetime: 1 day
SESSION_COOKIE_AGE = 24 * 60 * 60

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', 'django_q',
    'core', 'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.User"

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


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'postgres',
        "HOST": env('SQL_HOST'),
        "PORT": 5432,
        "USER": env('SQL_USER'),
        "PASSWORD": env('SQL_PASSWORD').strip(),
    }
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "backend_cache_table",
    }
}

Q_CLUSTER = {
    'name': 'backend',
    'workers': 4,
    'recycle': 100,
    'max_rss': 102400,  # 100 MB
    'max_attempts': 1,
    'retry': 7200,
    'timeout': 3600,
    'label': 'Django Q2',
    'orm': 'default',
    'poll': 1,
    'catch_up': False,
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGS_ROOT = BASE_DIR / 'logs'

LOGGING = {
    'version': 1,
    'formatters': {
        'with_separator': {
            'format': '=' * 50 + '\n[%(asctime)s] %(message)s',
            'datefmt': "%d.%b.%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(message)s',
            'datefmt': "%d.%b.%Y %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'django': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOGS_ROOT / 'django.error.log',
            'formatter': 'with_separator'
        },
        'db-file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOGS_ROOT / 'db.log',
            'formatter': 'simple'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOGS_ROOT / 'error.log',
            'formatter': 'with_separator'
        },
    },
    'loggers': {
        'django.request': {'handlers': ['console', 'django'], 'level': 'DEBUG', 'propagate': True},
        'backend': {'handlers': ['console', 'error'], 'level': 'INFO', 'propagate': True},
        # 'django.db': {'handlers': ['db-file', 'console'], 'level': 'DEBUG', 'propagate': True},
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'NON_FIELD_ERRORS_KEY': 'general',
    'UPLOADED_FILES_USE_URL': False,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# Format: (name, function, cron-schedule); name should be unique
# Should be enabled with manage.py command: enable-periodic
PERIODIC_TASKS = (
    ('Example', 'accounts.tasks.example_task', "*/10 * * * mon-fri"),  # Every ten minutes from monday to friday
)
