from django.shortcuts import render
from events.models import Event
from user_dashboard.models import UserEvent


def event_list(request):
    if request.GET:
        query = request.GET.get("search")
        if query:
            events = Event.objects.filter(title__icontains=query)
        else:
            events = Event.objects.none()
    else:
        events = Event.objects.all()
        
    return render(request, 'events/event_list.html', {'events': events})

