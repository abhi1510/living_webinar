from django.views import generic

from weblets.models import Weblet


class SearchWebletView(generic.ListView):
    template_name = 'search/weblets_result.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchWebletView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Weblets'
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Weblet.objects.search(query)
        return Weblet.objects.all()
