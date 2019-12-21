from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Presenter
from .forms import PresenterForm


class PresenterListView(LoginRequiredMixin, generic.ListView):
    template_name = 'presenters/list.html'
    paginate_by = 8

    def get_queryset(self):
        return Presenter.objects.filter(account=self.request.user.account)

    def get_context_data(self, *args, **kwargs):
        context = super(PresenterListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Presenter'
        return context


class PresenterDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'presenters/detail.html'

    def get_queryset(self):
        return Presenter.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(PresenterDetailView, self).get_context_data(**kwargs)
        context['page_title'] = 'Presenter'
        return context


class PresenterCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PresenterForm
    success_url = reverse_lazy('presenters:list')
    template_name = 'presenters/form.html'

    def get_queryset(self):
        return Presenter.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(PresenterCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Presenter'
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.account = self.request.user.account
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)


class PresenterUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = PresenterForm
    success_url = reverse_lazy('presenters:list')
    template_name = 'presenters/form.html'

    def get_queryset(self):
        return Presenter.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(PresenterUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Presenter'
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)


class PresenterDeleteView(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy('presenters:list')
    template_name = 'presenters/delete.html'

    def get_queryset(self):
        return Presenter.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(PresenterDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = 'Presenter'
        return context
