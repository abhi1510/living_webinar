from django.urls import path

from search.views import (
    SearchWebletView,
)

app_name = 'search'

urlpatterns = [
    path('', SearchWebletView.as_view(), name='query'),
]