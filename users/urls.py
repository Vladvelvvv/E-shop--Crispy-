from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name="profile"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path('forget-password/', views.ForgetPasswordView.as_view(), name="forget-password"),
    path('new-password/', views.NewPasswordView.as_view(), name="new-password"),
]