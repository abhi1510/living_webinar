from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save

from accounts.models import Account
from web.utils import unique_str_gen

User = settings.AUTH_USER_MODEL

PORTAL_STATUS_ENUM = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('deleted', 'Deleted'),
)


def picture_thumbnail_path(instance, filename):
    return 'weblets/{}/thumbnail/{}'.format(instance.title, filename)


def picture_large_path(instance, filename):
    return 'weblets/{}/large/{}'.format(instance.title, filename)


class Weblet(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, related_name='weblet')
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, default='draft', choices=PORTAL_STATUS_ENUM)
    picture_thumbnail = models.ImageField(upload_to=picture_thumbnail_path)
    picture_large = models.ImageField(upload_to=picture_large_path)
    tags = models.TextField(null=True, blank=True)
    webinar_recording_link = models.CharField(max_length=512)
    watcher_signup_required = models.BooleanField(default=False)
    publish_on_lw_website = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='weblet_created_by')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='weblet_modified_by')

    class Meta:
        ordering = ('-created_on', '-last_modified_on')

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Weblet)
def weblet_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_str_gen.unique_slug_generator(instance, instance.title)
