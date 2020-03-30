from django.urls import path
from .views import SignUp
from django.conf.urls import url, include

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]