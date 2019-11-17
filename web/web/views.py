from django.shortcuts import render, get_object_or_404

from weblets.models import Weblet
from presenters.models import Presenter


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


def test_view(_):
    from django.http import HttpResponse
    from django.template.loader import render_to_string
    from web.utils.email_sender import send_email
    msg_html = render_to_string('emails/test.html', {
        'email': 'some'
    })
    send_email('Test', msg_html, 'abhik.chy@gmail.com')
    return HttpResponse('Testing')
