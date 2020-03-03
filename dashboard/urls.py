
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout
<<<<<<< HEAD


=======
>>>>>>> ab50740b60181bb2e3396ef8bbb16aeb0aaa0cd0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('', include('pages.urls')),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls'))
]
