from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib import messages


def registration(request):
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")
            return redirect('registration')
        
        if len(username)>10:
            messages.error(request, "Username must less then 10 character")
            return redirect('registration')
        
        if not username.isalnum():
            messages.error(request, "Username only contain alphanumeric")
            return redirect('registration')
        
        if User.objects.filter(email=email):
            messages.error(request, "This email already have an account")
            return redirect('registration')
        
        if password1!=password2:
            messages.error(request, "Password didn't match")
            return redirect('registration')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = fname
        user.last_name = lname
        
        user.save()
        messages.success(request, "Your account has been successfully created")

        return redirect('sign-in')
        
    return render(request, 'authentication/registration.html')


def sign_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            authlogin(request, user)
            if request.GET.get('next', None):
                return redirect(request.GET['next'])
            return redirect('event-list')
        else:
            messages.error(request, 'Bad credential')
            return redirect('sign-in')
    return render(request, 'authentication/sign_in.html')


def sign_out(request):
    logout(request)
    messages.success(request, "You are successfully Sign out")
    return redirect('sign-in')