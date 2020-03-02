
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.forms import modelformset_factory
from django.shortcuts import render
from users.models import CustomUser

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def manage_authors(request):
    AuthorFormSet = modelformset_factory(CustomUser, fields=('email','is_active',))
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AuthorFormSet()
    return render(request, 'useredit.html', {'formset': formset})