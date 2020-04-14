<<<<<<< HEAD
"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
=======
>>>>>>> 122b803ea8dce60d9cc105925288e3f1c07fa08e
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from dashboard import views

def my_logout(request):
    logout(request)
    return redirect('login/')

app_name = 'dashboard'
urlpatterns = [
<<<<<<< HEAD
    url(r'^admin/', admin.site.urls),
    url(r'^gpa/', include('gpa.urls')),
=======
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('weather/', include('weather.urls')),    
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include("main.urls"), name='dashboard'),
    path('gpa/', include('gpa.urls')),


>>>>>>> 122b803ea8dce60d9cc105925288e3f1c07fa08e
]
