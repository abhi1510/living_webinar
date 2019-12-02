from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Watcher
from weblets.models import Weblet


class WatcherListView(LoginRequiredMixin, generic.ListView):
    template_name = 'watchers/list.html'
    paginate_by = 8

    def get_queryset(self):
        return Watcher.objects.filter(account=self.request.user.account)


def record_watcher(request, weblet_id):
    redirect_url = request.GET.get('redirect_url')
    weblet = get_object_or_404(Weblet, id=weblet_id)
    watcher = Watcher(
        account=weblet.account,
        weblet=weblet,
        source='LW'
    )
    if request.user.is_authenticated:
        watcher.user = request.user
    watcher.save()
    return redirect(redirect_url)
