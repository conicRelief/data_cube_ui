# Copyright 2016 United States Government as represented by the Administrator
# of the National Aeronautics and Space Administration. All Rights Reserved.
#
# Portion of this code is Copyright Geoscience Australia, Licensed under the
# Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License
# at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# The CEOS 2 platform is licensed under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Django settings for data_cube_ui project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j^rq-8z4l+b0cf(h3&+vjbz(bq3(d_-)h@==3vf&pz4wvz%xoh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MASTER_NODE = '127.0.0.1'

# Application definition

# TODO(map) : Change the URLs to BN1 and the port to 25.
BASE_HOST = "localhost:8000/"
ADMIN_EMAIL = "admin@ceos-cube.org"
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'

INSTALLED_APPS = [
    'apps.custom_mosaic_tool',
    'apps.water_detection',
    'apps.task_manager',
    'apps.tsm',
    'apps.fractional_cover',
    'data_cube_ui',
    'apps.accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.custom_mosaic_tool.testsuite',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'data_cube_ui.urls'

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\','/'),
            os.path.join(BASE_DIR, 'templates/custom_mosaic_tool').replace('\\','/'),
            os.path.join(BASE_DIR, 'templates/water_detection').replace('\\','/'),
            os.path.join(BASE_DIR, 'templates/tsm').replace('\\','/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'data_cube_ui.context_processors.countries',
            ],
        },
    },
]

WSGI_APPLICATION = 'data_cube_ui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'datacube',
	'USER': 'dc_user',
	'PASSWORD': 'dcuser1',
	'HOST': MASTER_NODE
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = [
    '/home/localuser/Datacube/data_cube_ui/static',
]

# CELERY STUFF

#master/slave machines.. master processes in the default queue, sends off tasks to workers.
CELERY_ROUTES = {'generate_mosaic_chunk': {'queue': 'chunk_processing'},
                 'generate_water_chunk': {'queue': 'chunk_processing'},
                 'generate_tsm_chunk': {'queue': 'chunk_processing'},
                 'generate_fractional_cover_chunk': {'queue': 'chunk_processing'}}

BROKER_URL = 'redis://' + MASTER_NODE + ':6379'
CELERY_RESULT_BACKEND = 'redis://' + MASTER_NODE + ':6379'
#CELERY_ACCEPT_CONTENT = ['application/json', 'yaml']
#CELERY_TASK_SERIALIZER = 'yaml'
#CELERY_RESULT_SERIALIZER = 'yaml'
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = True
CELERY_TIMEZONE = 'UTC'