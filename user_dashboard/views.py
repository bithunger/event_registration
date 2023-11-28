from django.shortcuts import render


def dashboard(request):
    return render(request, 'user_dashboard/dashboard.html')


def my_events(request):
    return render(request, 'user_dashboard/my_events.html')
