from .base import *

SECRET_KEY = 'django-insecure-hjpaby%k0judizw&#d@i!0o+^o1urgnbpq^oddjq=b@#16b+fx'

DEBUG = True

ALLOWED_HOSTS = ['*']

# static and media
# STATIC_URL = '/static/'

# if DEBUG:
#     STATICFILES_DIRS = [os.path.join( BASE_DIR, 'static' )]
# else:
#     STATIC_ROOT = os.path.join( BASE_DIR, 'static' )

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'