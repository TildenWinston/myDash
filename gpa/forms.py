from django import forms

from .models import Class

class ClassModelForm(forms.ModelForm):
    class Meta:
        model = Class
        fields =[
            'name',
            'year',
            'semester',
            'grade',
            'numeric_grade',
            'credit_hours',
        ]