from django.urls import path

from .views import (
    PortalList,
)

app_name = 'portals-api'

urlpatterns = [
    path('', PortalList.as_view(), name='list'),
]
