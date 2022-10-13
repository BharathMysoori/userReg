"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from userApp.views import *
from django.conf.urls.static import static #added 
from django.conf import settings #added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registerView,name='register'),
    
    path('login/',loginView,name='loginpage'),
    path('logout/',logoutView,name='logout'),
    path('',homeView,name='home'),
    #path('profile/<int:pk>',updateCustomer,name='update'),
    path('profile/',viewprofile,name='profile'),
    path('profile/<int:pk>',viewprofile,name='update'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
