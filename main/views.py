from django.shortcuts import render

def index(request):
    
    context = {
        'title': 'Crispy'
    }
    
    return render(request, "main/index.html", context)

def about(request):
    
    context = {
        'title': 'О нас'
    }
    
    return render(request, "main/about.html", context)