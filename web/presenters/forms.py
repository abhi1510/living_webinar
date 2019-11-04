from django import forms

from .models import Presenter


class PresenterForm(forms.ModelForm):
    class Meta:
        model = Presenter
        fields = ('full_name', 'title', 'company_name', 'about', 'linked_in_url',
                  'twitter_handle', 'picture_thumbnail', 'picture_large')
        widgets = {
            'linked_in_url': forms.Textarea(attrs={'rows': 2}),
            'twitter_handle': forms.Textarea(attrs={'rows': 2}),
            'about': forms.Textarea(attrs={'rows': 4}),
            # 'picture_thumbnail': forms.TextInput(attrs={'style': 'visibility:hidden'})

        }
