
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
    path('toDoList/', include('toDoList.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', my_logout, name="logout"),
    path('login/', include('login.urls')),
    path('logout/login/', include('login.urls')), #temporary workaround
]