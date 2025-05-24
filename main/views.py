from django.shortcuts import render

def index(request):
    
    context = {
        'title': 'Crispy',
        'class': 'index',
    }
    
    return render(request, "main/index.html", context)

def about(request):
    
    context = {
        'title': 'О нас',
        'class': 'index',
    }
    
    return render(request, "main/about.html", context)