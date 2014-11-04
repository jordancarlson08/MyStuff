"""
Django settings for django-mako-plus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&kpr$d=$+(5@)mp0xn3wobq-^_zpauhstwpm@0=s4iod5d1vbw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.User'

# AUTH_PROFILE_MODULE = 'account.UserProfile'

LOGIN_URL = '/login/'


#Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'iscore26@gmail.com'
EMAIL_HOST_PASSWORD = 'Ifihadnomorals26'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# EMAIL_HOST = 'mx-mail.digitallifemyway.com'
# EMAIL_HOST_USER = 'webmaster@digitallifemyway.com'
# EMAIL_PORT = 25
# EMAIL_USE_TLS = False
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Application definition

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')  


# MEDIA_ROOT = '/catalog/images/products/'
# MEDIA_URL = '/media/'



# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
#     'django.core.context_processors.tz',
#     'django.core.context_processors.request',
#     'django.contrib.messages.context_processors.messages',
#     'django_facebook.context_processors.facebook',
# )

# AUTHENTICATION_BACKENDS = (
#     'django_facebook.auth_backends.FacebookBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )



MIDDLEWARE_CLASSES = (
    # put your django middleware here - I'm listing some common ones
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # our custom base_app.controller middleware (can be last in the list)
    'base_app.controller.RequestInitMiddleware',
)

# our django applications
INSTALLED_APPS = (
    # put your django apps here - I'm listing the common ones
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # then list your custom apps

    #allauth stuff
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    'django_summernote',
    # 'django_facebook',
    'base_app',                # the base templates/css/javascript for all other apps
    'homepage',
    'manager',
    'account',
    'catalog',

    
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# django.db.backends.postgresql_psycopg2

# DATABASES = 
# 'default': {
#      'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': 'C:\Python33\db.sqlite3'
#    }
# }
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE':'django.db.backends.postgresql_psycopg2',
#        'NAME': 'mystuff',
#        'USER': 'postgres',
#        'PASSWORD': 'admin',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    BASE_DIR,  # THIS IS A SECURITY ISSUE AND SHOULD ONLY BE DONE FOR DEVELOPMENT - DURING DEPLOYMENT, GATHER ALL YOUR STATIC FILES INTO ONE DIRECTORY OUTSIDE THE PROJECT ROOT
)

# sample logging - the Mako controller (route_request) prints out to the log when in DEBUG mode.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
          'level': 'DEBUG',
          'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': DEBUG and 'DEBUG' or 'WARNING',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['null'],  # set this to 'console' to see all the DB queries being run
            'propagate': False,
            'level':'DEBUG',
        },
    },
}


###############################################################
###   Specific settings for the base_app Controller

# which of our apps will be used with the Mako engine. 
# typically this should be all of the custom apps of your project.
MAKO_ENABLED_APPS = (

    #allauth stuff
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'django_facebook',
    'django_summernote',
    'base_app',                # the base templates/css/javascript for all other apps
    'homepage',
    'manager',
    'account',
    'catalog',
    
)

# the default app/templates/ directory is always included in the template search path
# define any additional search directories here - this allows inheritance between apps
# absolute paths are suggested
MAKO_TEMPLATES_DIRS = [ 
  os.path.join(BASE_DIR, 'base_app', 'templates'),
]

# identifies where the Mako template cache will be stored, relative to each app
MAKO_TEMPLATES_CACHE_DIR = 'cached_templates/'

# the default app and page to render in Mako when the url is too short
# the search will go as follows for the url: http://www.yourserver.com/myurl/
#  1. /myurl/index       (see the MAKO_DEFAULT_PAGE below, this tries myurl as the app with default page)
#  2. /calculator/myurl  (see the MAKO_DEFAULT_APP below, this tries the default app with myurl as the page)
#  3. If none of these are found, a 404 error is returned
MAKO_DEFAULT_APP = 'homepage'
MAKO_DEFAULT_PAGE = 'index'  

# these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
MAKO_DEFAULT_TEMPLATE_IMPORTS = [
  'import os, os.path, re',
]

SUMMERNOTE_CONFIG = {
    # Change editor size
    'width': '100%',
    'height': '320',

    # Set editor language/locale
    'lang': 'en-US',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol', 'height']],
        
    ],

}


# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     "django.contrib.auth.backends.ModelBackend",
#     # `allauth` specific authentication methods, such as login by e-mail
#     "allauth.account.auth_backends.AuthenticationBackend"
# )
 
# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.core.context_processors.request",
#     "django.contrib.auth.context_processors.auth",
#     "allauth.account.context_processors.account",
#     "allauth.socialaccount.context_processors.socialaccount",
# )
 
# # auth and allauth settings
# LOGIN_REDIRECT_URL = '/'
# SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email', 'publish_stream'],
#         'METHOD': 'js_sdk'  # instead of 'oauth2'
#     }
# }
# FACEBOOK

# FACEBOOK_APP_ID = '415227401946294'
# FACEBOOK_APP_SECRET = '5159c001dc30d7c4950656ba8a3b4de8'


###  End of settings for the base_app Controller
################################################################
