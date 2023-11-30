from django.shortcuts import render, redirect
from events.models import Event
from django.contrib.auth.models import User
from user_dashboard.models import UserEvent
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'user_dashboard/dashboard.html')


@login_required
def my_events(request):
    my_events = UserEvent.objects.filter(user=request.user)
    return render(request, 'user_dashboard/my_events.html', {'my_events':my_events})


@login_required
def register_event(request, pk):
    user = User.objects.get(id=request.user.id)
    event = Event.objects.get(id=pk)
    
    try:
        UserEvent.objects.get(user=user, user_event=event)
        messages.error(request, "You already registered in this event")
    except:
        if event.slots>0:
            messages.error(request, "No slots available for this event")
                
        # create user event
        UserEvent.objects.create(user=user, user_event=event)
        messages.success(request, "Event registered successfully")
        # sub a event slot
        event.slots = int(event.slots)-1
        event.save()
    
    return redirect('my-events')


@login_required
def unregister_event(request, pk):
    # delete user event
    my_event = UserEvent.objects.get(id=pk)
    my_event.delete()
    messages.success(request, "Event unregistered successfully")
    
    # add a event slot
    event = Event.objects.get(id=my_event.user_event.id)
    event.slots = int(event.slots)+1
    event.save()
    
    return redirect('my-events')