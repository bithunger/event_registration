from django.shortcuts import render


def sign_in(request):
    return render(request, 'authentication/sign_in.html')


def registration(request):
    return render(request, 'authentication/registration.html')
