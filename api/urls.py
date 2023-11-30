from api import views
from django.urls import path

urlpatterns = [
    path('events', views.Get_events.as_view()),
    path('event-details/<int:pk>', views.Details_event.as_view()),
    path('user-events/<int:pk>', views.Get_user_events.as_view()),
    
    # user registration url
    path('user-registration', views.Registration.as_view()),
    path('user-event/registration', views.Event_registration.as_view()),
]
