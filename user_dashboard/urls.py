from django.urls import path, include
from user_dashboard import views

urlpatterns = [
    # user-dashboard
    path('', views.dashboard, name='dashboard'),
    path('my-events', views.my_events, name='my-events'),
]
