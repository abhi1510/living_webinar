from django.urls import path

from .views import (
    WebletListView,
    WebletDetailView,
    WebletCreateView,
    WebletUpdateView,
    WebletDeleteView,
)

app_name = 'weblets'

urlpatterns = [
    path('', WebletListView.as_view(), name='list'),
    path('<str:slug>/detail', WebletDetailView.as_view(), name='detail'),
    path('create', WebletCreateView.as_view(), name='create'),
    path('<str:slug>/update', WebletUpdateView.as_view(), name='update'),
    path('<str:slug>/delete', WebletDeleteView.as_view(), name='delete'),
]
