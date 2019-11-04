import jwt
import time

from django.conf import settings


def encode_data(payload):
    payload.update({'created': time.time()})
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm='HS256'
    ).decode('utf-8')


def decode_data(encoded_jwt):
    return jwt.decode(
        encoded_jwt,
        settings.SECRET_KEY,
        algorithms=['HS256']
    )
