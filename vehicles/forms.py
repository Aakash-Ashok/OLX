from django.contrib.auth.models import User
from vehicles.models import Vehicles
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
class RegistrationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["name","company","contact","km_driven","owner_type","price","location","img"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "company":forms.TextInput(attrs={"class":"form-control"}),
            "contact":forms.TextInput(attrs={"class":"form-control"}),
            "km_driven":forms.TextInput(attrs={"class":"form-control"}),
            "owner_type":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
        }