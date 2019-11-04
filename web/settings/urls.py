from django.urls import path

from .views import (
    home_view,
    account_update_view,
    user_add_view,
    user_update_view,
)

app_name = 'settings'

urlpatterns = [
    path('', home_view, name='home'),
    path('account-update', account_update_view, name='account_update'),
    path('user-add', user_add_view, name='user_add'),
    path('user-update', user_update_view, name='user_update'),
]
