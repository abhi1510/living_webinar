from .models import Weblet
from PIL import Image


def save_weblet(user):
    weblet = Weblet()
    weblet.account = user.account
    weblet.title = 'Weblet Save Test'
    weblet.description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
    weblet.picture_thumbnail = Image.open('')
    weblet.picture_large = Image.open('')
    weblet.webinar_recording_link = 'some link'
    weblet.created_by = user
    weblet.last_modified_by = user
    weblet.save()
