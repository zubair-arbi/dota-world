# development settings
import os

from dota_world.settings import BASE_DIR


DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#
# Development database with SQLITE3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# # Development database with MYSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dotadb',
#         'USER': 'dotauser',
#         'PASSWORD': 'doTaSecret',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
