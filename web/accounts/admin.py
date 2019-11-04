from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Account


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email']
    ordering = ('email',)
    exclude = ('username',)
    fieldsets = (
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'password', 'type', 'status')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}
         ),
    )


admin.site.register(Account)
admin.site.register(CustomUser, CustomUserAdmin)
