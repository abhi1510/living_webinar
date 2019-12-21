import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Weblet
from .forms import WebletForm
from .utils import save_weblet
from .services import get_webinars, get_recordings
from presenters.models import Presenter


class WebletListView(LoginRequiredMixin, generic.ListView):
    template_name = 'weblets/list.html'
    paginate_by = 8

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, *args, **kwargs):
        context = super(WebletListView, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'Weblets'
        context['presenters'] = Presenter.objects.filter(account=self.request.user.account)
        context['weblet_presenter'] = [{weblet.id: [p.id for p in weblet.presenters.all()]} for weblet in
                                       self.get_queryset()]
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
        context['page_title'] = 'Weblets'
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.account = self.request.user.account
        form.instance.created_by = self.request.user
        form.instance.last_modified_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class WebletUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = WebletForm
    success_url = reverse_lazy('weblets:list')
    template_name = 'weblets/form.html'

    def get_queryset(self):
        return Weblet.objects.filter(account=self.request.user.account)

    def get_context_data(self, **kwargs):
        context = super(WebletUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Weblets'
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
        context['page_title'] = 'Weblets'
        return context


def manipulate_weblet_presenter(request):
    weblet_id = request.POST.get('weblet_id')
    weblet = Weblet.objects.get(id=weblet_id)
    presenters = json.loads(request.POST.get('presenters'))
    for _id, status in presenters.items():
        presenter = Presenter.objects.get(id=_id)
        if status:
            weblet.presenters.add(presenter)
        else:
            weblet.presenters.remove(presenter)
    return redirect('weblets:list')


def zoom_import(request):
    context = dict()
    context['page_title'] = 'Weblets'
    token_type = request.session.get('token_type')
    access_token = request.session.get('access_token')

    if token_type and access_token:
        recordings = []
        status_code, json_data = get_webinars('richa.ahuja@livingwebinar.com', token_type, access_token)
        if status_code == 200:
            for w in json_data['webinars']:

                status_code, json_data = get_recordings(w['id'], token_type, access_token)
                if status_code == 200:
                    recording_link = json_data['share_url']
                else:
                    recording_link = ''
                recordings.append({
                    'id': w['id'],
                    'title': w['topic'],
                    'description': w['agenda'],
                    'recording_link': recording_link
                })
            context['webinars'] = recordings
        else:
            context['error'] = json_data['message']
    # context['webinars'] = [
    #     {'id': 1, 'title': 'Title 1', 'description': 'Some Description', 'recording_link': ''},
    #     {'id': 2, 'title': 'Title 2', 'description': 'Some Description', 'recording_link': 'xyz'},
    #     {'id': 3, 'title': 'Title 3', 'description': 'Some Description', 'recording_link': ''},
    #     {'id': 4, 'title': 'Title 4', 'description': 'Some Description', 'recording_link': 'mno'}
    # ]
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        recording_link = request.POST.get('recording_link')
        save_weblet(request.user, title, description, recording_link)
        return HttpResponse('OK')
    return render(request, 'weblets/zoom_import.html', context)
