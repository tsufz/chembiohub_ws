from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ID_PREFIX = "DEV"

WEBSERVICES_NAME='devapi'

LOGIN_REDIRECT_URL = "/#/projects/list"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cbh_chembl', # Or path to database file if using sqlite3.
        'USER': 'chembl', # Not used with sqlite3.
        'PASSWORD': 'chembl', # Not used witis oracle
        'HOST': '127.0.0.1', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432', # Set to empty string for default. Not used with sqlite3.
        'TEST_NAME' : 'tester_cbh_chembl'
    },
}

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/vagrant/chembiohub_ws/deployment/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/reg/'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
'/home/work/temp/src/ng-chem/',
)

# List of finder classes that know how to find static files in
# various locations.

INCHI_BINARIES_LOCATION = {"1.02" :"/home/vagrant/INCHI-1-BIN/linux/64bit/inchi-1"}

OPEN_BABEL_EXECUTABLE = "/home/vagrant/openbabel-2.3.2/build/bin/babel"


ANONYMOUS_USER_ID = -1

ALLOWED_HOSTS =["testserver"]



STATIC_ROOT = '/home/astretton/work/temp/deployment/static'
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
#'/home/vagrant/chembiohub_ws/src/ng-chem',
'/home/astretton/work/temp/src/ng-chem',

)

INCHI_BINARIES_LOCATION = {"1.02" :"/home/chembiohub/Tools/INCHI-1-BIN/linux/64bit/inchi-1"}

OPEN_BABEL_EXECUTABLE = "/home/chembiohub/Tools/openbabel-2.3.2/build/bin/babel"
