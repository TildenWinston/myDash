
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout
from src.django.django.shortcuts import redirect


def my_logout(request):
    logout(request)
    return redirect('login/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls'))
]
