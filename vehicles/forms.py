from django.contrib.auth.models import User
from vehicles.models import Vehicles
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model=User
        field=["username","Email","password1","password2"]



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

