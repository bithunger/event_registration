from django.urls import path, include
from events import views

urlpatterns = [
    # events
    path('', views.event_list, name='event-list'),
]
