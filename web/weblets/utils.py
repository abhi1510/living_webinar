import os

from .models import Weblet


def save_weblet(user, title, description, recording_link):
    weblet = Weblet()
    weblet.account = user.account
    weblet.title = title
    weblet.description = description

    default_image = os.path.join('weblets-images', 'preview_1556045620.png')
    weblet.picture_thumbnail = default_image
    weblet.picture_large = default_image

    weblet.webinar_recording_link = recording_link
    weblet.created_by = user
    weblet.last_modified_by = user
    weblet.save()
