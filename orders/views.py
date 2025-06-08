from django.shortcuts import render

def order(request):
    
     
    context = {
        'title': 'Заказ',
        'class': 'order',
    }
    
    return render(request, "orders/order.html", context)
