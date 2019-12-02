from django.db import models
from django.conf import settings

from accounts.models import Account
from weblets.models import Weblet

User = settings.AUTH_USER_MODEL


class Watcher(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, related_name='watchers')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    weblet = models.ForeignKey(Weblet, on_delete=models.CASCADE)
    referring_URL = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=100)
    data = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now=True)
    last_modified_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'watcher weblet-{}'.format(self.weblet)
