from django.urls import path

from .views import (
    PortalList,
    PortalDetailView,
)

app_name = 'portals-api'

urlpatterns = [
    path('', PortalList.as_view(), name='list'),

    path('<int:_id>', PortalDetailView.as_view(), name='detail'),
]
