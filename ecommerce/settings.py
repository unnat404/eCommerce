"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# ===========================================================================================================
# METHOD-1(implementation-1) : for security of SECRET_KEY :: AS ENVIRONMENT VARIABLE
# SECRET_KEY = os.environ['SECRET_KEY']
# ===========================================================================================================
# METHOD-1(implementation-2)(this is the way, i will use, if sucessful) : for security of SECRET_KEY :: AS ENVIRONMENT VARIABLE
SECRET_KEY = config('SECRET_KEY')

# ===========================================================================================================
# METHOD-2 : for security of SECRET_KEY :: FROM A FILE WHICH WILL BE GITIGNORED
# with open('<path to txt file containing secret key>') as f:
#     SECRET_KEY=f.read().strip()
# ===========================================================================================================

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1","digiecom.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store', # yaha usne 'store.apps.StoreConfig' some thing kiya tha butb his should also work i think 

]

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

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

############################################
# DATABASES = {
#     'default': {
#         'ENGINE': config('db_ENGINE'),
#         'NAME': config('db_NAME'),
#         'USER': config('db_USER') ,
#         'PASSWORD': config('db_PASSWORD') ,
#         'HOST': config('db_HOST') ,
#         'PORT': config('db_PORT') 
#     }
# }
############################################



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True





# Note : this step can be different ,
# since we defined our static files' ka location differently than in the project, I think)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
# print("\n-----\n base dir is : "+str(BASE_DIR))
# print(BASE_DIR/'static')

# added by unnat 
STATICFILES_DIRS=[
    BASE_DIR / 'static' ,
    BASE_DIR / 'store/static/store',
    # os.path.join(BASE_DIR,'static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')

MEDIA_URL='/images/'
# media root and url can be differnet as we have stored our images ina different position
# MEDIA_ROOT = BASE_DIR / 'store/static/images'
#  
# MEDIA_ROOT = BASE_DIR / 'static/images' 

MEDIA_ROOT = os.path.join(BASE_DIR,"store/static/store/images")
# MEDIA_ROOT = os.path.join(BASE_DIR,"static/images")


# os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

