from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    sign_up_view,
    sign_up_option_view,
    sign_up_success_view,
    verify_email_view,
    sign_up_complete_view,
    login_view,
)

app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('sign-up', sign_up_view, name='sign_up'),
    path('sign-up-option', sign_up_option_view, name='sign_up_option'),
    path('sign-up-success', sign_up_success_view, name='sign_up_success'),
    path('verify-email/<str:token>', verify_email_view, name='verify_email'),
    path('sign-up-complete', sign_up_complete_view, name='sign_up_complete'),
]
