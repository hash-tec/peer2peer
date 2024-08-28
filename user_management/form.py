from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ClearableFileInput
from django.contrib.auth.models import User
from .models import CustomerUser

class SignupForm(UserCreationForm):

    class Meta:
        model = CustomerUser
        fields =["first_name", "last_name", "email", "username", "password1", "password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = CustomerUser
        fields = ["pfp"]

from django import forms

class DobForm(forms.ModelForm):
    class Meta:
        model = CustomerUser  # Replace with your actual model
        fields = ['dob']

    dob = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'  # Add Bootstrap or other CSS classes if needed
            }
        ),
        label='Date of Birth',
        required=True,
    )

    dob = forms.DateField(required=False)

class BioForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ["bio"]
    
class AddressForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ["address"]
    


