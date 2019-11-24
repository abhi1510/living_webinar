from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Tag


class TagListView(LoginRequiredMixin, generic.ListView):
    template_name = 'tags/list.html'
    paginate_by = 8

    def get_queryset(self):
        return Tag.objects.filter(account=self.request.user.account)
