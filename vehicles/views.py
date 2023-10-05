from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from vehicles.forms import *
from vehicles.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registartion Succesfull")
            return redirect("login")
        else:
            messages.error(request,"Registration failed")
            return render(request,"registration.html",{"form":form})

