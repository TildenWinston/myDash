from django import forms
from django.forms import ModelForm, TextInput
from .models import City, Zipcode

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder

class ZipForm(ModelForm):
    class Meta:
        model = Zipcode
        fields = ['zip', 'user']
        widgets = {
            'zip': TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Zipcode e.g. 22904'}),
            'user': forms.HiddenInput()
        } #updates the input class to have the correct Bulma class and placeholder 