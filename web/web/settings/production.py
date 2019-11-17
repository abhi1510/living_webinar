from .base import *

HOST = 'http://ec2-18-190-105-126.us-east-2.compute.amazonaws.com'

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
