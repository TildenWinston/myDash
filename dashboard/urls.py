from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect


def my_logout(request):
    logout(request)
    return redirect('login/')

app_name = 'dashboard'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('weather/', include('weather.urls')),    
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include("main.urls"), name='dashboard'),
    path('gpa/', include('gpa.urls'))
,    
]
