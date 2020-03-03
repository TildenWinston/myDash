
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    #path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls'))
]
