from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import USER_STATUS_CHOICES
from accounts.forms import AccountForm

from .forms import UserAddForm, UserUpdateForm


@login_required(login_url='accounts:login')
def home_view(request):
    user = request.user
    context = {
        'page_title': 'Settings',
        'account': user.account,
        'user': user,
        'account_form': AccountForm(instance=user.account),
        'user_add_form': UserAddForm(),
        'user_change_form': UserUpdateForm(instance=user),
    }
    return render(request, 'settings/home.html', context)


@login_required(login_url='accounts:login')
def account_update_view(request):
    if request.method == 'POST':
        form = AccountForm(instance=request.user.account, data=request.POST)
        if form.is_valid():
            form.save()
    return redirect('settings:home')


@login_required(login_url='accounts:login')
def user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    return redirect('settings:home')


@login_required(login_url='accounts:login')
def user_add_view(request):
    logged_in_user = request.user
    if logged_in_user.type == 'admin':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.instance.account = logged_in_user.account
            form.instance.type = 'author'
            form.instance.status = USER_STATUS_CHOICES[0][0]
            form.instance.created_by = logged_in_user
            form.instance.last_modified_by = logged_in_user
            form.save()
        else:
            messages.error(request, form.errors)
    return redirect('settings:home')
