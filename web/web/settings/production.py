from .base import *

# TODO: change this to prod URL
HOST = 'http://localhost:8001'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'livingwebinar_db',
        'HOST': 'database-livingwebinar.cg5pev8vjomf.us-east-2.rds.amazonaws.com',
        'PORT': 3306,
        'USER': 'lw_admin',
        'PASSWORD': 'secret2success'
    }
}

