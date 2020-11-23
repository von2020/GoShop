from Goshop2.settings.base import *

# overide base.py settings here

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTD = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

try:
    from Goshop2.settings.local import *
except:
    pass