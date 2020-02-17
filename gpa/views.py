from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Class
from django.utils import timezone

# Create your views here.

class ClassView(generic.ListView):
    template_name = 'gpa/list.html'
    context_object_name = 'class_set'
    def get_queryset(self):
        return Class.objects.all()

class ClassCreate(generic.CreateView):
    template_name = 'gpa/classes.html'
    model = Class
    fields = '__all__'
    
    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return HttpResponseRedirect('list/')