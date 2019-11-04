from django import forms

from .models import Weblet


class WebletForm(forms.ModelForm):
    class Meta:
        model = Weblet
        fields = ('title', 'description', 'status', 'picture_thumbnail', 'picture_large', 'tags',
                  'webinar_recording_link', 'watcher_signup_required', 'publish_on_lw_website')
        labels = {
            'publish_on_lw_website': 'Publish on LW website'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'tags': forms.Textarea(attrs={'rows': 3}),
        }
