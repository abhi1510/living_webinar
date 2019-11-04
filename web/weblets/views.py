from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Weblet
from .forms import WebletForm


class WebletListView(LoginRequiredMixin, generic.ListView):
    template_name = 'weblets/list.html'
    paginate_by = 8

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, *args, **kwargs):
        context = super(WebletListView, self).get_context_data(*args, **kwargs)
        return context


class WebletDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'weblets/detail.html'

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(WebletDetailView, self).get_context_data(**kwargs)
        return context


class WebletCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = WebletForm
    success_url = reverse_lazy('weblets:list')
    template_name = 'weblets/form.html'

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(WebletCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.account = self.request.user.account
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)


class WebletUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = WebletForm
    success_url = reverse_lazy('weblets:list')
    template_name = 'weblets/form.html'

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(WebletUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)


class WebletDeleteView(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy('weblets:list')
    template_name = 'weblets/delete.html'

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(WebletDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = 'Presenter Delete'
        return context
