"""
URL configuration for olx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehicles.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name="index"),
    path('signup/',RegistrationView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('home/',Index2View.as_view(),name="home"),
    path('add/',VehicleCreateView.as_view(),name="add-vehicle"),
    path('list/',VehicleListView.as_view(),name="list-vehicle")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
