from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import  HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout as auth_logout


from carts.models import Cart
from common.mixins.cache_mixin import CacheMixin
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserPasswordChangeForm, UserRegistrationForm

class ProfileView(LoginRequiredMixin, CacheMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Данные профиля успешно обновлены')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Профиль"
        context["class"] = "profile"
        context["profile"] = True
        orders_cache = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch("orderitem_set",queryset=OrderItem.objects.select_related("product"))).order_by("-id")
        context["orders"] = self.set_get_cache(orders_cache, f"user_{self.request.user.id}_orders", 60*5)
        return context
    

class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    
    def get_success_url(self):
        redirect_page = self.request.POST.get('next')
        if redirect_page and redirect_page != reverse_lazy('users:logout'):
            return redirect_page
        return reverse_lazy('main:index')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        
        user = form.get_user()
        
        if user:
            auth.login(self.request, user)
            if session_key:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)

                messages.success(self.request, f"{user.username}, Вы вошли в аккаунт")

                return HttpResponseRedirect(self.get_success_url())
                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Вход"
        context['class'] = "profile"
        context['login'] = True
        return context

class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)

class RegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')
    
    def form_valid(self, form):
        session_key = self.request.session.session_key 
        user = form.instance
        
        if user:
            form.save()
            auth.login(self.request, user)
            
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            
            messages.success(self.request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        context["class"] = "profile"
        context["registration"] = True
        return context
    
class NewPasswordView(PasswordChangeView):
    template_name = "users/new-password.html"
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:profile')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Пароль успешно изменен")
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменение пароля"
        context["class"] = "profile"
        context["profile"] = True
        return context

class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Восстановление пароля"
        context['class'] = "profile"
        context['login'] = True
        return context

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Пароль сброшен"
        context['class'] = "profile"
        context['login'] = True
        return context
    
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Изменение пароля"
        context['class'] = "profile"
        context['login'] = True
        return context
    
class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Пароль изменен"
        context['class'] = "profile"
        context['login'] = True
        return context
        
    

