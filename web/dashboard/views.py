from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def dashboard_view(request):
    context = {
        'page_title': 'Dashboard',
        'weblets_count': request.user.account.weblet.count(),
        'presenters_count': request.user.account.presenter.count(),
        'portals_count': request.user.account.portal.count(),
        'authors_count': request.user.account.users.count(),
        'watchers_count': request.user.account.watchers.count()
    }
    return render(request, 'dashboard/dashboard.html', context)
