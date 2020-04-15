from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),  #the path for our index view
    path('dashapp/', views.dashapp, name='dashapp'),
    path('delete/<path:zip>/', views.delete, name='delete'),
]