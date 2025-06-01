from django.shortcuts import render

from goods.models import Products
from goods.utils import q_search

def cart(request):
    
    context = {
        'title': 'Корзина',
        'class': 'catalog',   
    }
    
    return render(request, "carts/cart.html", context=context)

def cart_add(request, product_id):
    ...

def cart_remove(request, product_id):
    ...

def cart_change(request, product_id):
    ...


