from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1n2g5l5tpqm@m4hcy@r#n=t-qow%an-3_=&82i@qh#&ongo8)7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    # 'drf_auto',
    'django_filters',
    "taggit",
    "volunteer",
    "users",
    "partner",
    "shop",
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

ROOT_URLCONF = 'config.urls'

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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    ]
}

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = "users.Users"

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TAGGIT_CASE_INSENSITIVE = True

REST_FRAMEWORK_AUTO = {
    'DOCS': {
        'HIDE_DOCS': False,
        'SERIALIZERS_ATTR_NAME': 'docs_serializer_classes',
        'EXCLUDE_FIELDS_ATTR_NAME': 'docs_exclude_fields',
        'SERIALIZER_DOC_ATTR': 'doc_method_fields_classes',
        'PARSER_CLASS': 'drf_auto.autodocs.parsers.DefaultParser'
    },
    'AUTO_REST': {
        'EXCEPTIONS': {
            'PROCESS_EXCEPT': True,
            'PROCESS_EXCEPT_HANDLER': None,
            'CODE_EXCEPTION_LIST': 400,
            'STATUS_EXCEPTION_LIST': 400,
            'EXCEPTION_LIST': ['rest_framework.serializers.ValidationError'],
            'EXCEPTION_DICT': {
                'rest_framework.serializers.ValidationError': {
                    'status': 400,
                    'code': 400,
                    'message': 'Ошибка валидации. Неверные данные.',
                    'fields': {'status': 'status', 'code': 'code', 'message': 'message', 'data': 'data'},
                    'data_attr': 'detail',
                },
            },
        },
    },
    'SERIALIZER_DOC_CODES': {'common': {}, 'specific': {}},
    'SERIALIZERS_RESPONSE_FIELD': 'serializer_classes',
    'SERIALIZERS_REQUEST_FIELD': 'serializer_classes',
    'SERIALIZERS_REQUEST_KEY': 'in',
    'SERIALIZERS_RESPONSE_KEY': 'out'
}