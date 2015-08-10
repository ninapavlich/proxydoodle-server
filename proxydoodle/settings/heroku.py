from proxydoodle.settings.base import *

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']
SITE_ID = 2

DATABASES = herokuify.get_db_config()   # Database config