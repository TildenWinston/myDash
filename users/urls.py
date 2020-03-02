from django.urls import path
from .views import SignUp, manage_authors

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('edit/', manage_authors, name="edit"),
]