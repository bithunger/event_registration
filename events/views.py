from django.shortcuts import render
from events.models import Event
from user_dashboard.models import UserEvent


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})



