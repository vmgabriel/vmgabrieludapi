"""Settings Project"""

import os
import environ
import django_heroku
from pathlib import Path
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG", default=False)
MODE = (env("MODE", default="production")).lower()

ALLOWED_HOSTS = ["127.0.0.1", ".herokuapp.com"]


USER_APPLICATIONS = [
    "accounts.apps.AccountsConfig",
    "api.apps.ApiConfig",
]
EXTERNALS_APPLICATIONS = [
    "versatileimagefield",
    "rest_framework_jwt",
    "rest_framework_jwt.blacklist",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",

    "rest_framework",
] + USER_APPLICATIONS + EXTERNALS_APPLICATIONS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 15,
     "DEFAULT_PERMISSION_CLASSES": [
         "rest_framework.permissions.IsAuthenticated",
         "rest_framework.permissions.IsAdminUser",
     ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
     )
}

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": env.db(),
    "extra": env.db("SQLITE_URL", default="sqlite:////tmp/my_db.sqlite3"),
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static/"),
)


# Redirect when i can load
AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_URL = "pages:home"
LOGOUT_REDIRECT_URL = "pages:home"


# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


JWT_AUTH = {
    "JWT_SECRET_KEY": SECRET_KEY,
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_INSIST_ON_KID": False,
    "JWT_TOKEN_ID": "include",
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
    "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_payload",
    "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_token",
    "JWT_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_create_payload",
    "JWT_PAYLOAD_GET_USERNAME_HANDLER": "rest_framework_jwt.utils.jwt_get_username_from_payload_handler",
    "JWT_PAYLOAD_INCLUDE_USER_ID": True,
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": timedelta(seconds=300),
    "JWT_ALLOW_REFRESH": True,
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_create_response_payload",
    "JWT_AUTH_COOKIE": None,
    "JWT_AUTH_COOKIE_DOMAIN": None,
    "JWT_AUTH_COOKIE_PATH": "/",
    "JWT_AUTH_COOKIE_SECURE": True,
    "JWT_AUTH_COOKIE_SAMESITE": "Lax",
    "JWT_IMPERSONATION_COOKIE": None,
    "JWT_DELETE_STALE_BLACKLISTED_TOKENS": False,
}

WHITENOISE_USE_FINDERS = True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Django Heroku
print(f"MODE - {MODE}")


if MODE == "production":
    django_heroku.settings(locals())
