from unicodedata import category
from django.shortcuts import get_list_or_404, render

from goods.models import Products

def catalog(request, category_slug):
    
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    context = {
        'title': 'Каталог',
        'class': 'catalog',
        'products': products,
        
    }
    
    return render(request, "goods/catalog.html", context=context)

def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'title': 'Карта товара',
        'class': 'catalog',
        'product': product,
    }
    
    return render(request, "goods/product.html", context=context)