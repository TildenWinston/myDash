from django.urls import path

from . import views

app_name = 'gpa'

urlpatterns = [
    path('classes/', views.ClassCreate.as_view(), name='classes'),
    path('classes/list/', views.ClassView.as_view(), name='list'),
]