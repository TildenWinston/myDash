from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #path('', views.MainPageView.as_view(), name='home'),
    path('', include('calendarApp.urls')),
]