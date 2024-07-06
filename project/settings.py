"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&45a6h5v7p@b6(!-u=+$)#m9jya8=s^&0&ygo8b@j(-+ez&9*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

#security stripe

STRIPE_SECRET_KEY_TEST = 'sk_test_51PHTnvHXSU4CQitgjRYN9MNjaNE7rs5rBkf61Drpq6DZvq2CLb4k9JegsAIy10zMYdiisv7XeNgyR0GvdX0UPJrF00IVN6sJVa'
STRIPE_PUBLISHABLE_KEY_TEST = 'pk_test_51PHTnvHXSU4CQitgBhon58rOWZ3Yf0hsxj84KNkGHntNOTG7kAoD1WTqf6XZ1k1cYXPvd7U6MIcIoH7LgeU95LA000aLmMPiq6'
STRIPE_WEBHOOK_SECRET_TEST = 'whsec_7b1bc214b39d4fa0b51a610650d5c04396f61f25d14839605f70c145edc49a6f'
REDIRECT_DOMAIN = 'http://127.0.0.1:8000'
PRODUCT_PRICE = 'price_1PWjhrHXSU4CQitg17cMI3qL' 

EXCHANGE_RATE_USD_TO_EGP = 1
# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'home',
    'blog',
    'about',
    'contact',
    'shop',
    'search',
    'bootstrap4',
    'django_filters',

    
]
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

DJSTRIPE_USE_NATIVE_JSONFIELD = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts.middleware.CustomSessionMiddleware',  # تأكد من وجود هذا الوسيط بشكل صحيح
    # 'accounts.middleware.PreventAdminLoginMiddleware', 
    'accounts.middleware.DisableAdminLoginMiddleware', 
    'accounts.middleware.DisableAdminLogoutMiddleware',


]




ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    # "/var/www/static/",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

LOGIN_URL = '/login/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER='mahmoudnabil11112@gmail.com'
EMAIL_HOST_PASSWORD='hopb jpkw buoc lpwo'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_COOKIE_NAME = 'main_sessionid'

ADMIN_SESSION_COOKIE_NAME = 'admin_sessionid'
