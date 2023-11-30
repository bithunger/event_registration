import json
from django.http import Http404, JsonResponse
from events.models import Event
from user_dashboard.models import UserEvent
from django.contrib.auth.models import User
from .serializers import EventSerializer, UserEventSerializer, RegisterSerializer, UserEventRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



# List of all events
class Get_events(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=201)


    
# Details of a specific event
class Details_event(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=201)



# User's registered events
class Get_user_events(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        user_events = UserEvent.objects.filter(user=user)
    
        if not user_events.exists():
            return JsonResponse({'error': 'Does not found any registered events'}, status=404)
        
        serializer = UserEventSerializer(user_events, many=True)
        return Response(serializer.data, status=201)
 
    

# User registration for an event
class Registration(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




# User registration for an event
class Event_registration(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404
        
    def post(self, request):
        user = User.objects.get(pk=request.POST.get('user'))
        pk=request.POST.get('user_event')
        event = self.get_object(pk)
        user_events = UserEvent.objects.filter(user=user, user_event=event)
        serializer = UserEventRegisterSerializer(data=request.data)
        
        if not user_events.exists():
            if event.slots<=0:
                return JsonResponse({'error': 'No slots available for this event'}, status=404)
            
            if serializer.is_valid():
                serializer.save()
                event.slots = int(event.slots)-1
                event.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return JsonResponse({'error': 'You have already registered'}, status=404)