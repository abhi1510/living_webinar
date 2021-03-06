import base64
import requests

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

from .models import CustomUser, USER_STATUS_CHOICES
from .forms import SignUpForm
from web.utils.token_manager import decode_data


def sign_up_option_view(request):
    if request.method == 'POST':
        request.session['sign_up_option'] = request.POST['signUpOption']
        return redirect('accounts:sign_up')
    return render(request, 'accounts/sign-up-options.html')


def sign_up_view(request):
    sign_up_as = request.session.get('sign_up_option')
    if sign_up_as is None:
        return redirect('accounts:sign_up_option')
    print(sign_up_as)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.instance.type = sign_up_as
            form.instance.status = USER_STATUS_CHOICES[0][0]
            form.save()
            del request.session['sign_up_option']
            return redirect('accounts:sign_up_success')
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign-up.html', {'form': form})


def sign_up_success_view(request):
    return render(request, 'accounts/sign-up-success.html')


def verify_email_view(_, token):
    data = decode_data(token)
    # verify token expiration time as data has created key
    user = get_object_or_404(CustomUser, pk=data.get('id'))
    user.is_active = True
    user.status = USER_STATUS_CHOICES[1][0]
    user.save()
    return redirect('accounts:sign_up_complete')


def sign_up_complete_view(request):
    return render(request, 'accounts/sign-up-complete.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next:
                    return redirect(_next)
                else:
                    if user.type == 'admin' or user.type == 'author':
                        return redirect('dashboard:dashboard')
                    else:
                        return redirect('home')
    else:
        form = AuthenticationForm(request=request)
    return render(request, 'accounts/login.html', context={'form': form})


def obtain_token(request):
    authorization_code = request.GET.get('code')
    zoom_token_ep = 'https://zoom.us/oauth/token'
    app_redirect = '{}/accounts/oauth/token'.format(settings.HOST)

    client_id = settings.OAUTH_PROVIDERS['ZOOM']['CLIENT_ID']
    client_secret = settings.OAUTH_PROVIDERS['ZOOM']['CLIENT_SECRET']

    encoded_bytes = base64.b64encode('{}:{}'.format(client_id, client_secret).encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    auth = 'Basic {}'.format(encoded_str)

    headers = {'Authorization': auth}
    url = '{}?grant_type=authorization_code&code={}&redirect_uri={}'.format(zoom_token_ep,
                                                                            authorization_code,
                                                                            app_redirect)
    res = requests.post(url, headers=headers)

    if res.status_code == 200:
        token = res.json()
        request.session['token_type'] = token.get('token_type')
        request.session['access_token'] = token.get('access_token')
        request.session['refresh_token'] = token.get('refresh_token')
    return redirect('weblets:zoom_import')


def refresh_token():
    pass


def revoke_token():
    pass
