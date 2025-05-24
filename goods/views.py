from django.shortcuts import render

def catalog(request):
    
    context = {
        'title': 'Каталог',
        'class': 'catalog'
    }
    
    return render(request, "goods/catalog.html", context)

def product(request):
    
    context = {
        'title': 'Карта товара',
        'class': 'catalog',
    }
    
    return render(request, "goods/product.html", context)