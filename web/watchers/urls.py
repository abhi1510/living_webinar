from django.urls import path

from .views import (
    WatcherListView,
    record_watcher,
)

app_name = 'watchers'

urlpatterns = [
    path('', WatcherListView.as_view(), name='list'),
    path('record_watcher/<int:weblet_id>', record_watcher, name='record_watcher'),
]
