from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crispy'
        context['class'] = 'index'
        context['index'] = True
        return context

class AboutView(TemplateView):
    template_name = "main/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        context['class'] = 'index'
        context['about'] = True
        return context

