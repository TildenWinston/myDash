from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .forms import ClassModelForm
from .models import Class, GPA

from django.http import Http404

# Create your views here.

def calc(self):
    total = 0
    creds = 0
    for c in Class.objects.all():
        total += c.numeric_grade * c.credit_hours
        creds += c.credit_hours
    return total/creds

class ClassListView(ListView):
    template_name = 'gpa/class_list.html'
    queryset = Class.objects.all() # <blog>/<modelname>_list.html
    ontext_object_name = 'class_set'
    def get_queryset(self):
        return Class.objects.all()

class ClassDetailView(DetailView):
    template_name = 'gpa/class_detail.html'
    queryset = Class.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Class, id=id_)

class ClassUpdateView(UpdateView):
    template_name = 'gpa/class_create.html'
    form_class = ClassModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Class, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClassDeleteView(DeleteView):
    template_name = 'gpa/class_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Class, id=id_)

    def get_success_url(self):
        return reverse('gpa:class-list')

class ClassCreateView(generic.CreateView):
    template_name = 'gpa/class_create.html'
    form_class = ClassModelForm
    queryset = Class.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClassView(generic.ListView):
    template_name = 'gpa/list.html'
    context_object_name = 'class_set'
    queryset = Class.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ClassView, self).get_context_data(**kwargs)
        context['classes'] = self.queryset
        context['GPA'] = GPA.objects.all()
        # And so on for more models
        return context