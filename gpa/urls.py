from django.urls import path
from .views import (
    ClassCreateView,
    ClassDeleteView,
    ClassDetailView,
    ClassListView,
    ClassUpdateView,
   
)

app_name = 'gpa'

urlpatterns = [
    path('', ClassListView.as_view(), name='class-list'),
    path('create/', ClassCreateView.as_view(), name='class-create'),
    path('<int:id>/', ClassDetailView.as_view(), name='class-detail'),
    path('<int:id>/update/', ClassUpdateView.as_view(), name='class-update'),
    path('<int:id>/delete/', ClassDeleteView.as_view(), name='class-delete'),
]
