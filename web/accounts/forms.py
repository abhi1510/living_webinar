from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from .models import CustomUser, Account


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('organization_name', 'country', 'state', 'city', 'street_address', 'zip', 'phone')
        widgets = {
            'street_address': forms.Textarea(attrs={'rows': 6})
        }



