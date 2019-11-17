from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

from .models import Portal, PortalWeblet
from .forms import PortalForm, PortalWebletForm


@login_required(login_url='accounts:login')
def portal_list_view(request):
    object_list = Portal.objects.filter(account=request.user.account)
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        portals = paginator.page(page)
    except PageNotAnInteger:
        portals = paginator.page(1)
    except EmptyPage:
        portals = paginator.page(paginator.num_pages)
    context = {
        'object_list': portals,
        'portal_form': PortalForm(),
        'portal_form_action': reverse_lazy('portals:create'),
    }
    return render(request, 'portals/list.html', context)


@login_required(login_url='accounts:login')
def portal_create_view(request):
    if request.method == 'POST':
        form = PortalForm(data=request.POST)
        if form.is_valid():
            form.instance.account = request.user.account
            form.instance.created_by = request.user
            form.instance.last_modified_by = request.user
            form.save()
    return redirect('portals:list')


@login_required(login_url='accounts:login')
def portal_update_view(request, slug):
    instance = get_object_or_404(Portal, slug=slug)
    portal_weblets = PortalWeblet.objects.filter(account=request.user.account, portal=instance)
    page = request.GET.get('page', 1)
    paginator = Paginator(portal_weblets, 6)
    try:
        portal_weblets = paginator.page(page)
    except PageNotAnInteger:
        portal_weblets = paginator.page(1)
    except EmptyPage:
        portal_weblets = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = PortalForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.instance.last_modified_by = request.user
            form.save()
            return redirect('portals:list')
    form = PortalForm(instance=instance)
    return render(request, 'portals/update.html', {
        'portal_form': form,
        'portal_form_action': reverse_lazy('portals:update', kwargs={'slug': slug}),
        'portal_weblet_form': PortalWebletForm(portal_id=instance.id, account_id=request.user.account.id),
        'portal_weblet_form_action': reverse_lazy('portals:portal_weblet_add', kwargs={'portal_slug': slug}),
        'portal_weblets': portal_weblets
    })


@login_required(login_url='accounts:login')
def portal_delete_view(request, slug):
    instance = get_object_or_404(Portal, slug=slug)
    if request.method == 'POST':
        instance.delete()
        return redirect('portals:list')
    return render(request, 'portals/delete.html', {'object': instance})


@login_required(login_url='accounts:login')
def portal_preview_view(request, slug):
    instance = get_object_or_404(Portal, slug=slug)
    context = {
        'instance': instance
    }
    return render(request, 'portals/preview.html', context)


@login_required(login_url='accounts:login')
def portal_weblet_add_view(request, portal_slug):
    instance = get_object_or_404(Portal, slug=portal_slug)
    if request.method == 'POST':
        form = PortalWebletForm(data=request.POST)
        if form.is_valid():
            form.instance.portal = instance
            form.instance.account = request.user.account
            form.instance.created_by = request.user
            form.instance.last_modified_by = request.user
            form.save()
    return redirect(reverse_lazy('portals:update', kwargs={'slug': instance.slug}))


@login_required(login_url='accounts:login')
def portal_weblet_update_rank_view(request, portal_weblet_id):
    portal_weblet = PortalWeblet.objects.get(id=portal_weblet_id)
    portal = portal_weblet.portal
    if request.POST:
        portal_weblet.weblet_rank = int(request.POST.get('weblet_rank', 0))
        portal_weblet.save()
    return redirect(reverse_lazy('portals:update', kwargs={'slug': portal.slug}))


@login_required(login_url='accounts:login')
def portal_weblet_remove_view(_, portal_weblet_id):
    portal_weblet = PortalWeblet.objects.get(id=portal_weblet_id)
    portal = portal_weblet.portal
    portal_weblet.delete()
    return redirect(reverse_lazy('portals:update', kwargs={'slug': portal.slug}))
