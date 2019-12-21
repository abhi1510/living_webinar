from django.shortcuts import render


def home_view(request):
    context = {
        'page_title': 'Analytics'
    }
    return render(request, 'analytics/home.html', context)
