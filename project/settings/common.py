# -*- coding: utf-8 -*-
# Django settings for nadezhdanova project.

from os.path import dirname, join, abspath

# from logging import LOGGING


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Andrey Kutyrev", "andrey.kutyrev@gmail.com"),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = [
    "nadezhdanova.com"
]

TIME_ZONE = "Europe/Moscow"

LANGUAGES = (
    ("ru", "Russian"),
    ("en", "English"),
)
LANGUAGE_CODE = "ru"
PROJECT_LANGUAGE_CODE = "en"

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = abspath(join(dirname(__file__), "../"))

MEDIA_ROOT = join(PROJECT_ROOT, "media/")
MEDIA_URL = "/media/"

STATIC_ROOT = join(PROJECT_ROOT, "sitestatic/")
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    join(PROJECT_ROOT, "static"),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",

    "compressor.finders.CompressorFinder",
)

# Make this unique, and don"t share it with anybody.
SECRET_KEY = "jsjto=gg_pn$1)v-ljb$bdh60&rsd=&i468(*k8+xv8d&eh)^z"

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "project.middleware.LocaleMiddleware",
    "project.middleware.AdminLocalMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = "project.urls.base"

# Python dotted path to the WSGI application used by Django"s runserver.
WSGI_APPLICATION = "project.wsgi.application"

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, "templates/"),
)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "suit",
    "django.contrib.admin",
    "django.contrib.admindocs",

    # 3rd party.
    "imperavi",
    "south",
    "gunicorn",
    "sorl.thumbnail",
    "compressor",
    "flatblocks",
    "suit_ckeditor",

    # project apps.
    "activities",
    "works",
    "i18n",
)

LOCALE_PATHS = (
    join(dirname(__file__), "../../locale"),
)

# 3rd party apps settigns.

SUIT_CONFIG = {
    "ADMIN_NAME": "Nadezhdanova.com",
    "MENU_EXCLUDE": ("auth.group", "auth", "sites"),
}

COMPRESS_PRECOMPILERS = (
    ("text/less", "lessc {infile} {outfile}"),
)

# IMPERAVI_CUSTOM_SETTINGS = {
#     "wym": True
# }
