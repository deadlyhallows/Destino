"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bgi^ydi)g=8d4j0i#umgk@s(c6d322trm25(7w2*#r9z^q)6=i'

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
    'tourism',
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

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'evicharya@gmail.com'
EMAIL_HOST_PASSWORD = 'qwerty@1234'
DEFAULT_FROM_EMAIL = 'evicharya@gmail.com'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SALT = '7ngHbu55jc'
KEY = 'oYKYBJEf'


# Payu----settings, use for Production only

# The value should be one of the items from the list ['production', 'test']
# PAYMENT_MODE = "production"#default will be "test"

# merchant_key from payu. default value will be included builtin in the package.
# MERCHANT_KEY = "xxxxxxxx"

# merchant_salt from payu. default value will be included builtin in the package.
# MERCHANT_SALT = "xxxxxxxx"

# Where to redirect while transaction is succeeded.
# SUCCESS_URL = "www.example.com/success/" #default will be "http://127.0.0.1:8000/payubiz-success/"

# Where to redirect while transaction got failure.
# FAILURE_URL = "www.example.com/failure/" #default will be "http://127.0.0.1:8000/payubiz-failure/"

# Where to redirect while transaction got canceld
# CANCEL_URL = "www.example.com/cancel/" #default will be "http://127.0.0.1:8000/payubiz-cancel/"
PAYU_INFO = {
    'merchant_key': "test merchant key",

    'merchant_salt': "test merchant salt",
    # for production environment use 'https://secure.payu.in/_payment'
    'payment_url': 'https://test.payu.in/_payment',
    'surl': 'http://example.com/pay-success/',
    'furl': 'http://example.com/failure/',
    'curl': 'http://example.com/cancel/',
}
PAID_FEE_AMOUNT = 1
PAID_FEE_PRODUCT_INFO = "Message showing product details."
PAYMENT_URL_TEST = 'https://test.payu.in/_payment'
PAYMENT_URL_LIVE = 'https://secure.payu.in/_payment'
SERVICE_PROVIDER = "payu_paisa"