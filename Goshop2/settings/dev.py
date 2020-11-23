from Goshop2.settings.base import *

# overide base.py settings here

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