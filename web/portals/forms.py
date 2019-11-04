from django import forms

from weblets.models import Weblet
from .models import Portal, PortalWeblet


class PortalForm(forms.ModelForm):
    class Meta:
        model = Portal
        fields = ('title',)


class PortalWebletForm(forms.ModelForm):
    class Meta:
        model = PortalWeblet
        fields = ('weblet', 'weblet_rank')
        widgets = {
            'weblet_rank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Portal Rank'}),
        }

    def __init__(self, *args, **kwargs):
        portal_id = kwargs.pop('portal_id', None)
        super(PortalWebletForm, self).__init__(*args, **kwargs)
        self.fields['weblet'].queryset = Weblet.objects.exclude(
                id__in=[pw.weblet.id for pw in PortalWeblet.objects.filter(portal=portal_id)])
