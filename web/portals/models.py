from django.db import models
from django.conf import settings
from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver

from web.utils import unique_str_gen
from accounts.models import Account
from weblets.models import Weblet

User = settings.AUTH_USER_MODEL

PORTAL_STATUS_ENUM = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('deleted', 'Deleted'),
)


class Portal(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, related_name='portal')
    title = models.CharField(max_length=512)
    status = models.CharField(max_length=10, default='draft', choices=PORTAL_STATUS_ENUM)
    slug = models.SlugField(unique=True, blank=True)
    sharable_script = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='portal_created_by')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='portal_modified_by')

    def __str__(self):
        return self.title

    def weblets_count(self):
        return self.portal_weblet.all().count()


class PortalWeblet(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, related_name='portal_weblet')
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE, related_name='portal_weblet')
    weblet = models.ForeignKey(Weblet, on_delete=models.CASCADE, related_name='portal_weblet')
    weblet_rank = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='portal_weblet_created_by')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='portal_weblet_modified_by')

    class Meta:
        ordering = ('weblet_rank',)

    def __str__(self):
        return '{} - {}'.format(self.portal, self.weblet)

    @classmethod
    def get_last_weblet_rank(cls, account):
        aggr = cls.objects.filter(account=account).aggregate(Max('weblet_rank'))
        return aggr.get('weblet_rank__max') or 0


@receiver(pre_save, sender=Portal)
def portal_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = unique_str_gen.unique_slug_generator(instance, instance.title)
