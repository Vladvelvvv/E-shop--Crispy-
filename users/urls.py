from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name="profile"),
    
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    
    path('password-change/', views.NewPasswordView.as_view(), name="password_change"),
    
    path('password-reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"), 
    path('password-reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete")
]