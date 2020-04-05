from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ClassModelForm
from .models import Class

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

def class_index(request):
    total = 0
    creds = 0
    grade = 0
    for c in Class.objects.all():
        total += c.grade_weight
        creds += c.credit_hours
        grade = total/creds
    grade = str(round(grade, 3))
    context = {
        'grade': grade,
        'class_list': Class.objects.all(),
        }
    return render(request, 'gpa/class_list.html', context)    