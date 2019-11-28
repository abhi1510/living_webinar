from django import forms

from weblets.models import Weblet
from .models import Portal, PortalWeblet


class PortalForm(forms.ModelForm):
    class Meta:
        model = Portal
        fields = ('title', 'status')


class PortalWebletForm(forms.ModelForm):
    class Meta:
        model = PortalWeblet
        fields = ('weblet',)

    def __init__(self, *args, **kwargs):
        portal_id = kwargs.pop('portal_id', None)
        account_id = kwargs.pop('account_id', None)
        super(PortalWebletForm, self).__init__(*args, **kwargs)
        weblets = Weblet.objects.filter(account=account_id)
        self.fields['weblet'].queryset = weblets.exclude(
                id__in=[pw.weblet.id for pw in PortalWeblet.objects.filter(portal=portal_id)])
