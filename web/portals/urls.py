from django.urls import path

from .views import (
    portal_list_view,
    portal_create_view,
    portal_update_view,
    portal_delete_view,
    portal_preview_view,
    portal_weblet_add_view,
    portal_weblet_remove_view,
    portal_weblet_update_rank_view,

    portal_sharable_script
)

app_name = 'portals'

urlpatterns = [
    path('', portal_list_view, name='list'),
    path('create', portal_create_view, name='create'),
    path('<str:slug>/update', portal_update_view, name='update'),
    path('<str:slug>/delete', portal_delete_view, name='delete'),
    path('<str:slug>/preview', portal_preview_view, name='preview'),
    path('<str:slug>/sharable_script', portal_sharable_script, name='sharable_script'),

    path('<str:portal_slug>/portal-weblet-add', portal_weblet_add_view, name='portal_weblet_add'),
    path('<int:portal_weblet_id>/portal-weblet-remove', portal_weblet_remove_view, name='portal_weblet_remove'),
    path('<int:portal_weblet_id>/portal-weblet-update-rank', portal_weblet_update_rank_view,
         name='portal_weblet_update_rank'),
]
