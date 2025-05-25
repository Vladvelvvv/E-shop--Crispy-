from unicodedata import category
from django.shortcuts import render

from goods.models import Products

def catalog(request):
    
    products = Products.objects.all()
    
    context = {
        'title': 'Каталог',
        'class': 'catalog',
        'products': products,
    }
    
    return render(request, "goods/catalog.html", context)

def product(request):
    
    products = Products.objects.all()
    
    context = {
        'title': 'Карта товара',
        'class': 'catalog',
        'products': products,
    }
    
    return render(request, "goods/product.html", context)