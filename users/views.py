from django.shortcuts import render

def profile(request):
    
    context = {
        'title': 'Профиль',
        'class': 'profile',
    }
    
    return render(request, "users/profile.html", context=context)

def login(request):
    
    context = {
        'title': 'Вход',
        'class': 'profile',
    }
    
    return render(request, "users/login.html", context=context)

def logout(request):
    
    ...

def registration(request):
    
    context = {
        'title': 'Регистрация',
        'class': 'profile',
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

