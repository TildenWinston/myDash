from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from dashboard import views

def my_logout(request):
    logout(request)
    return redirect('')


app_name = 'dashboard'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('main.urls'),name='dashboard'),
    path('todo/', include('todo.urls')),
    path('weather/', include('weather.urls')),    
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('calendarApp/', include("calendarApp.urls"), name = 'calendarApp'),
    path('gpa/', include('gpa.urls')),
  
    # path('dashboard/', include("main.urls"), name='dashboard'),
    
    #path('todolist/', include('todo.urls')),


]
