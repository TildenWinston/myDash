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
    #path('dashboard/', include('todo.urls'),name='dashboard'),
    path('todo/', include('main.urls')),
    path('weather/', include('weather.urls')),    
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
<<<<<<< HEAD
    path('dashboard/', include("main.urls")),
    path('calendarApp/', include("calendarApp.urls")),
    path('dashboard/', include("main.urls"), name='dashboard'),
    path('gpa/', include('gpa.urls')),
  
=======
    # path('dashboard/', include("main.urls"), name='dashboard'),
    path('gpa/', include('gpa.urls')),
    path('todolist/', include('todo.urls')),


>>>>>>> c5b27415593212d434a17ba252c050c8421561b3
]
