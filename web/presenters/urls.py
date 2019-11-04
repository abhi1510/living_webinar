from django.urls import path

from .views import (
    PresenterListView,
    PresenterDetailView,
    PresenterCreateView,
    PresenterUpdateView,
    PresenterDeleteView
)

app_name = 'presenters'

urlpatterns = [
    path('', PresenterListView.as_view(), name='list'),
    path('<int:pk>/detail', PresenterDetailView.as_view(), name='detail'),
    path('create', PresenterCreateView.as_view(), name='create'),
    path('<int:pk>/update', PresenterUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', PresenterDeleteView.as_view(), name='delete')
]
