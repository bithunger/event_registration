from django.urls import path, include
from user_dashboard import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # user-dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('register-event/<int:pk>', views.register_event, name='register-event'),
    path('unregister-event/<int:pk>', views.unregister_event, name='unregister-event'),
    path('my-events', views.my_events, name='my-events'),
]
