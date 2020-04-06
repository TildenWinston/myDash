from django.urls import path
from .views import (
    ClassCreateView,
    ClassDeleteView,
    ClassUpdateView,
    ClassList,
)

app_name = 'gpa'

urlpatterns = [
    path('', ClassList, name='class-list'),
    path('create/', ClassCreateView.as_view(), name='class-create'),
    path('<int:id>/update/', ClassUpdateView.as_view(), name='class-update'),
    path('<int:id>/delete/', ClassDeleteView.as_view(), name='class-delete'),
   
]
