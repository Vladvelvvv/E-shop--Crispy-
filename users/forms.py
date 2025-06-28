from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm


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
    birth_day = forms.DateInput()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "birth_day",
            "username",
            "email",
        )
        
    image = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    birth_day = forms.DateField(required=False)
    email = forms.CharField(required=False)
    
class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        fields =(
            "old_password",
            "new_password1",
            "new_password2"
        )
        
    old_password = forms.CharField(required=False)
    new_password1 = forms.CharField(required=False)
    new_password2 = forms.CharField(required=False)


