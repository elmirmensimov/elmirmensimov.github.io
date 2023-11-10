from django.contrib.auth.models import User
from .models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    pass



