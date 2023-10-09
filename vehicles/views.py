from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,ListView
from vehicles.forms import *
from vehicles.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name="index.html"


class Index2View(TemplateView):
    template_name="index_2.html"




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

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usr=authenticate(request,username=username,password=password)
            if usr:
                login(request,usr)
                messages.success(request,"Login succesful")
                return redirect("home")
            else:
                messages.error(request,"Login failed")
                return render(request,"login.html",{"form":form})
            

def logoutview(request):
    logout(request)
    return redirect("login")



class VehicleCreateView(View):

    def get(self,request,*args,**kwargs):
        form=VehicleCreateForm()
        return render(request,"add_vehicle.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            Vehicles.objects.create(**form.cleaned_data,user=request.user)
            return redirect("list-vehicle")
        else:
            return render(request,"add_vehicle.html",{"form":form})


class VehicleListView(ListView):
    template_name="list_vehicle.html"
    model=Vehicles
    context_object_name="vehicle"
    def get_queryset(self):
        qs=Vehicles.objects.filter(user=self.request.user)
        return qs