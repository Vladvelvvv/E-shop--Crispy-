from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products

def catalog(request, category_slug):
    
    page = request.GET.get('page', 1)
    
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    paginator = Paginator(products, 8)
    current_page = paginator.page(int(page))
    
    context = {
        'title': 'Каталог',
        'class': 'catalog',
        'products': current_page,
        'slug_url': category_slug,    
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