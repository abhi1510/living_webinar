from django.urls import path

from .views import (
    manipulate_weblet_presenter
)

app_name = 'weblets-api'

urlpatterns = [
    path('manipulate_weblet_presenter', manipulate_weblet_presenter, name='manipulate_weblet_presenter'),
]
