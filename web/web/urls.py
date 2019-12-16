from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, weblet_detail_view, portal_detail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),
    path('webcast/<str:slug>', weblet_detail_view, name='weblet_detail_view'),
    path('portal_detail', portal_detail, name='portal_detail'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard', include('dashboard.urls', namespace='dashboard')),
    path('weblets/', include('weblets.urls', namespace='weblets')),
    path('presenters/', include('presenters.urls', namespace='presenters')),
    path('watchers/', include('watchers.urls', namespace='watchers')),
    path('portals/', include('portals.urls', namespace='portals')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('settings/', include('settings.urls', namespace='settings')),
    path('search/', include('search.urls', namespace='search')),

    path('api/weblets/', include('weblets.api.urls', namespace='weblets-api')),
    path('api/portals/', include('portals.api.urls', namespace='portals-api')),
    path('api/tags/', include('tags.urls', namespace='tags')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
