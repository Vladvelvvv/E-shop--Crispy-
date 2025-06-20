from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView

from goods.models import Products
from goods.utils import q_search

class CatalogView(ListView):
    template_name = "goods/catalog.html"
    model = Products
    paginate_by = 4
    context_object_name = "products"
    
    def get_queryset(self):
        
        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")
        
        if category_slug == 'all':
            products = super().get_queryset()
            
        elif query:
            products = q_search(query)
        else:
            products = super().get_queryset().filter(category__slug=category_slug)
        
        if on_sale:
            products = products.filter(discount__gt=0)
            
        if order_by and order_by != 'default':
            products = products.order_by(order_by)
            
        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Каталог"
        context["class"] = "catalog"
        context["catalog"] = True
        context["slug_url"] = self.kwargs.get("category_slug")
        return context

class ProductView(DetailView):
    
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    
    def get_object(self):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Товар"
        context['class'] = "catalog"
        context['catalog'] = True
        return context
