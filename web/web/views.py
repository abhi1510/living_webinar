from django.shortcuts import render, get_object_or_404

from weblets.models import Weblet


def home_view(request):
    context = {
        'object_list': Weblet.objects.filter(publish_on_lw_website=True, status='published')
    }
    return render(request, 'public/home.html', context)


def weblet_detail_view(request, slug):
    weblet = get_object_or_404(Weblet, slug=slug)
    context = {
        'object': weblet
    }
    return render(request, 'public/weblet_detail.html', context)


def portal_detail(request):
    return render(request, 'public/portals.html')
