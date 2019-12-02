from django.shortcuts import render


def home_view(request):
    context = {
        'weblets': ['weblets', 'Weblet 1', 'Weblet 2', 'Weblet 3', 'Weblet 4', 'Weblet 5', 'Weblet 6'],
        'watcher_counts': ['watcher_counts', 5, 3, 0, 7, 9, 2]
    }
    return render(request, 'analytics/home.html', context)
