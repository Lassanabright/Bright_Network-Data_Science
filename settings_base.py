"""
ABSOLUTE_IMPORT:
Without this errors: "No module named schedules" because we have a celery.py
file in the same package as the settings.py, which shadows the global celery
package
"""
from __future__ import absolute_import
import os
import sys


from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j^&+ct(a53+&2bb-1vj4hf$8jex+86vp$t+aqar5s#5!de(_a1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.algoliasearch',
    'django_mptt_admin',
    'ckeditor',
    'ckeditor_uploader',
    'filebrowser',
    'web',
    'bootstrapform',
    'django.contrib.admin',
    'salesforce',
    'rest_framework',
    'rest_framework.authtoken',
    'cal',
    'compressor',
    'htmlmin',
    'ajax_select',
    'Machine_Learning',
]

# Compressor settings.
COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', '/usr/local/bin/lessc {infile} {outfile}'),
)

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']

HTML_MINIFY = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


MIDDLEWARE = [
    'htmlmin.middleware.MarkRequestMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'web.middleware.RedirectsDataMiddleware',
    'web.middleware.RequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'brightnetwork.urls'

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
                'web.context_processors.template_defaults',
            ],
        },
    },
]

WSGI_APPLICATION = 'brightnetwork.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brightnetwork',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = [
    "salesforce.router.ModelRouter"
]


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'web.utils.drupal.DrupalSHA512PasswordHasher',
]

AUTH_USER_MODEL = "web.User"

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ML_FILES = os.path.join(BASE_DIR, 'Machine_Learning/files/')

ALGOLIA = {
    'APPLICATION_ID': 'Z7100UG4XZ',
    'API_KEY': '4a3b4915b2a94187d2a677ee30d1983d'
}

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# Authentication system
LOGIN_REDIRECT_URL = '/welcome/'
LOGIN_URL = '/login/'

# Mailgun
MAILGUN_AUTH = ("api", "key-b6f2a2f3a357d09de70de91fd9d5fd55")
MAILGUN_MSG_ENDPOINT = "https://api.mailgun.net/v3/mg.brightnetwork.co.uk/messages"

# CELERY SETTINGS
BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/London'
CELERYD_CONCURRENCY = 1

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', '-', 'Undo', 'Redo'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image'],
            ['Embed'],
            ['Youtube'],
            ['Source']
        ],
        'extraPlugins': ','.join(
            [
                # Extra plugins go here.
                'embed',
                'youtube'
            ]),
    }
}

# Email settings
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@mg.brightnetwork.co.uk'
SERVER_EMAIL = 'logging@brightnetwork.co.uk'
EMAIL_HOST_PASSWORD = 'e6fcbfd30247bf2d684aad4fda2c6766'

# Emails: Account verification
VERIFY_EMAIL_HTML = 'mail/verification_email.html'
VERIFY_EMAIL_PLAIN = 'mail/verification_email.txt'
VERIFY_EMAIL_SUBJECT = 'Bright Network - confirm your email address'
VERIFY_FROM_EMAIL = 'Bright Network <help@brightnetwork.co.uk>'

# Emails: Tablet signup
TABLET_SIGNUP_SUBJECT = 'Welcome to Bright Network. Get started today!'
TABLET_SIGNUP_EMAIL_FROM = 'Bright Network <hello@brightnetwork.co.uk>'

# Emails: Contact us
CONTACT_US_EMAILS_FROM = 'Bright Network <employers@brightnetwork.co.uk>'
CONTACT_US_EMPLOYER_EMAIL_SUBJECT = 'Thank you for getting in touch with Bright Network'
CONTACT_US_ADMIN_EMAIL_SUBJECT = 'Employer Website Enquiry: %s'
CONTACT_US_ADMIN_EMAIL_ADDRESS = 'employers@brightnetwork.co.uk'

# Emails: Calendar alerts
ALERT_EMAILS_FROM = 'Bright Network Alerts <alerts@brightnetwork.co.uk>'

JOB_ALERT_EMAIL_HTML = 'emails/job_alert_email.html'
JOB_ALERT_EMAIL_PLAIN = 'emails/job_alert_email.txt'
JOB_ALERT_SUBJECT = 'Deadline Alert - %s - %s'

EVENT_ALERT_EMAIL_HTML = 'emails/event_alert_email.html'
EVENT_ALERT_EMAIL_PLAIN = 'emails/event_alert_email.txt'
EVENT_ALERT_SUBJECT = 'Event Alert - %s - %s'

ROLLING_DEADLINE_EMAIL_HTML = 'emails/rolling_deadline_email.html'
ROLLING_DEADLINE_EMAIL_PLAIN = 'emails/rolling_deadline_email.txt'
ROLLING_DEADLINE_EMAIL_SUBJECT = 'Your Rolling Deadlines Reminder Alert'

CAL_CONFIRMTATION_EMAIL_HTML = 'emails/cal_confirmation_email.html'
CAL_CONFIRMTATION_EMAIL_PLAIN = 'emails/cal_confirmation_email.txt'
CAL_CONFIRMATION_EMAIL_SUBJECT = 'Your Bright Network Alerts: All Confirmed'

DEFAULT_EMPLOYER_HERO_PICTURE = os.path.join(
    STATIC_URL, "img/default_employer_hero_pic.jpg")

# Google API key
GOOGLE_API_KEY = 'AIzaSyD3FtkQAs_hgZGIbEXNXXsFaITyBz_oVnA'

DEFAULT_FROM_EMAIL = "Bright Network <help@brightnetwork.co.uk>"

# Celery beat scheduling for the calendar
CELERYBEAT_SCHEDULE = {
    'confirmation-email': {
        'task': 'cal.tasks.send_pending_confirmation_emails',
        'schedule': crontab()
    },
    'search-ranks-recalc-every-monday': {
        'task': 'web.tasks.search_rank_recalc',
        'schedule': crontab(minute=0, hour=1, day_of_week='monday')
    },
    'pull-salesforce-accounts-data-every-5-mins': {
        'task': 'web.tasks.pull_sf_accounts_data',
        'schedule': crontab(minute="*/5")
    },
    'process-tablet-api-signups-every-5-mins': {
        'task': 'web.tasks.process_tablet_api_signups',
        'schedule': crontab(minute="*/5")
    },
    'check-signups-health-every-10-mins': {
        'task': 'web.tasks.check_signups_health',
        'schedule': crontab(minute="*/10")
    },    
    'check-signups-health-every-day': {
        'task': 'web.tasks.signups_health_daily_report',
        'schedule': crontab(hour=23, minute=0)
    },
    'delete-obsolete-form-logs-every-day': {
        'task': 'web.tasks.delete_obsolete_form_logs',
        'schedule': crontab(hour=1, minute=0)
    },
}

CELERY_SEND_TASK_ERROR_EMAILS = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    "values": {
        "BACKEND": 'redis_cache.RedisCache',
        "LOCATION": 'localhost:6379',
    },
    "profile_statuses": {
        "BACKEND": 'redis_cache.RedisCache',
        "LOCATION": 'localhost:6379',
    },
    "user_segments": {
        "BACKEND": 'redis_cache.RedisCache',
        "LOCATION": 'localhost:6379',
    },
}

# Template defaults
DEFAULT_META_DESCRIPTION = 'All the best graduate careers advice, jobs and events from Bright Network'

# django-filebrowser settings
FILEBROWSER_DIRECTORY = "files_live/public/"

# media subdirectory, where postcode data resides
POSTCODES_DIR = "postcodes/"

# media subdirectory, where local copies of user CVs are stored
# each CV will be stored in user's own subdir, named after user's profile id
CV_DIR = "cv/"

# Django admins
ADMINS = [
    ('Tom', 'thomas.brightwell@brightnetwork.co.uk'),
    ('Saemie', 'saemie@chouchane.com'),
    ('Leonid', 'side2k.svc@gmail.com'),
    ('Tom W', 'tom.webb@brightnetwork.co.uk'),
]

# Maximum number of GET/POST parameters that will be read before a
# SuspiciousOperation (TooManyFieldsSent) is raised.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000


# reporter API settings
REPORTER_API_MAX_ITEMS_PER_QUERY = 10000

# how many days to store FormLogEntries
FORM_LOGS_STORE_DAYS = 30


# REST framework settings
# doc: http://www.django-rest-framework.org/api-guide/authentication/#how-authentication-is-determined
# we're turning off basic authentication class because API is protected by
# nginx's basic auth. And if basic auth class is added here, then it will 
# respond with 403 on each request with basic auth headers
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# this URL should be redefined in environment-related settings file
BASE_URL = "https://brightnetwork.co.uk/"


# this flag is for ability to disable job applications syncing to
# SalesForce on save() call on environments not connected to proper
# SF instances, like staging and preprod
# by default it is True and should be set to False in the staging and 
# preprod settings
JOBAPPS_SYNC_TO_SF = True


# this setting disables tablet signup processing initiated right after
# signup is received. Should be set to True if anything goes wrong with that
# the code is in web.api.v1.TabletSignupRequests.post method
DISABLE_QUICK_TABLET_SIGNUPS = False
