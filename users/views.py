from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

def profile(request):
    
    context = {
        'title': 'Профиль',
        'class': 'profile',
    }
    
    return render(request, "users/profile.html", context=context)

def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Вход',
        'class': 'profile',
        'form' : form,
    }
    
    return render(request, "users/login.html", context=context)

def logout(request):
    
    auth.logout(request)
    return redirect(reverse('main:index'))

def registration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Регистрация',
        'class': 'profile',
        'form' : form,
    }
    
    return render(request, "users/registration.html", context=context)
    

def forget_password(request):
    
    context = {
        'title': 'Восстановление пароля',
        'class': 'profile',
    }
    
    return render(request, "users/forget-password.html", context=context)

def new_password(request):
    
    context = {
        'title': 'Восстановление пароля',
        'class': 'profile',
    }
    
    return render(request, "users/new-password.html", context=context)

