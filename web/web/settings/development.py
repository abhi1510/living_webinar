from .base import *

HOST = 'http://localhost:8001'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}

OAUTH_PROVIDERS = {
    'ZOOM': {
        'CLIENT_ID': '2AAjch3rQ0mRQdRZmK4UlA',
        'CLIENT_SECRET': 'KRX4uo5QZvzRInijtm2tqhvzUVHf21dj'
    }
}
