from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from vehicles.forms import *
from vehicles.models import *
# Create your views here.


class RegistrationView(View):
    