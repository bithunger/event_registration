from django.urls import path, include
from authentication import views

urlpatterns = [
    # authentication
    path('registration', views.registration, name='registration'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-out', views.sign_out, name='sign-out'),
]
