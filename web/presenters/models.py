from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save

from accounts.models import Account
from web.utils import unique_str_gen

User = settings.AUTH_USER_MODEL


def picture_thumbnail_path(instance, filename):
    return 'presenters/{0}/thumbnail/{1}'.format(instance.full_name, filename)


def picture_large_path(instance, filename):
    return 'presenters/{0}/large/{1}'.format(instance.full_name, filename)


class Presenter(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, related_name='presenter')
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    linked_in_url = models.TextField(null=True, blank=True)
    twitter_handle = models.TextField(null=True, blank=True)
    picture_thumbnail = models.ImageField(null=True, blank=True, upload_to=picture_thumbnail_path)
    picture_large = models.ImageField(null=True, blank=True, upload_to=picture_large_path)
    slug = models.SlugField(unique=True, blank=True)

    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='presenter_created_by')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='presenter_modified_by')

    def __str__(self):
        return self.full_name


@receiver(pre_save, sender=Presenter)
def presenter_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_str_gen.unique_slug_generator(instance, instance.full_name)
