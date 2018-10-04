from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brightnetwork',
        'USER': '',
        'PASSWORD': '',
    },
    'salesforce': {
        'ENGINE': 'salesforce.backend',
        'CONSUMER_KEY': "3MVG92H4TjwUcLlLvIMWkOuic3bghXoT89wYARA1X8CmkPCksfpZO4_y8pbkS2NbyRmFg9or_f0sNAJfZBHh_",
        'CONSUMER_SECRET': "8958883973426606149",
        'USER': "tech@brightnetwork.co.uk.test",
        'PASSWORD': "7$88I-=pheTh=XarUne@" + "NYYZ0zYQolEiOaoDD3ZilosW", # password and token
        'HOST': "https://test.salesforce.com",
    }
}

# DEBUG = False
#
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

ALGOLIA.update({
    "INDEX_SUFFIX": "dev"
})

LOGGING = {
    "version": 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

EMAIL_SUBJECT_PREFIX = "[django-dev]"
JOBAPPS_SYNC_TO_SF = False
