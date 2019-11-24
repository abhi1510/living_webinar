from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, weblet_detail_view, test_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name='home'),
    path('webcast/<str:slug>', weblet_detail_view, name='weblet_detail_view'),

    # temp
    path('test', test_view),

    path('dashboard', include('dashboard.urls', namespace='dashboard')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('presenters/', include('presenters.urls', namespace='presenters')),
    path('api/tags/', include('tags.urls', namespace='tags')),
    path('weblets/', include('weblets.urls', namespace='weblets')),
    path('portals/', include('portals.urls', namespace='portals')),
    path('settings/', include('settings.urls', namespace='settings')),


    path('api/weblets/', include('weblets.api.urls', namespace='weblets-api')),
    path('api/portals/', include('portals.api.urls', namespace='portals-api')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
