from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template.defaultfilters import first

from users.models import User

class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    username = forms.CharField(
        widget=forms.TextInput()
    )
    password =  forms.CharField(
        widget=forms.PasswordInput(),
    )
    
        
class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "birth_day",
            "email",
            "password1",
            "password2",
        )
        
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    birth_day = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()