from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registration/', views.registration, name="registration"),
    path('forget-password/', views.forget_password, name="forget-password"),
    path('new-password/', views.new_password, name="new-password"),
]