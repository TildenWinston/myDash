from django.contrib import admin
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path, include # Might be removable

def my_logout(request):
    logout(request)
    return redirect('login/')
app_name = 'mydash'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('weather/', include('weather.urls')),
    path('weather/', include('weather.urls')),
    path('', include('todo.urls')),
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard', include("main.urls")),
    
]
