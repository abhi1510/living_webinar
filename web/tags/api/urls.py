from django.urls import path

from .views import (
    TagList,
)

app_name = 'tags-api'

urlpatterns = [
    path('', TagList.as_view(), name='list'),
]
