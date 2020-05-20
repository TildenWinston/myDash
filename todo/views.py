from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.clickjacking import xframe_options_exempt
#from django.http import HttpResponseRedirect

import requests

from .models import Todo
from .forms import TodoForm


@xframe_options_exempt
def index(request):
    todo_list = Todo.objects.order_by('id')

    #print(todo_list[0].user)

    user_todo_list = []

    for todo in todo_list:
        if(todo.user == request.user):
            user_todo_list.append(todo)

    form = TodoForm()

    context = {'todo_list' : user_todo_list, 'form' : form}

    return render(request, 'todo/todo.html', context)

@xframe_options_exempt
def todoapp(request):
    todo_list = Todo.objects.order_by('id')
    #print(todo_list[0].user)
    #print(request.user)

    user_todo_list = []

    for todo in todo_list:
       #print("win") 
       if(todo.user == request.user):
            user_todo_list.append(todo)

    form = TodoForm()

    context = {'todo_list' : user_todo_list, 'form' : form}

    return render(request, 'todo/todoapp.html', context)


@require_POST
@xframe_options_exempt
def addTodo(request):
    print(request.META['HTTP_REFERER'])

    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'], user=request.user)
        new_todo.save() 

    #return HttpResponseRedirect(request.path_info)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))