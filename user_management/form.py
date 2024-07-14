from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerUser
class SignupForm(UserCreationForm):

    class Meta:
        model = CustomerUser
        fields =["first_name", "last_name", "username", "password1", "password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)



