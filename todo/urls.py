from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('app', views.todoapp, name='todoapp'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]