from django.db import models
from django.db.models import Sum
from django.forms import ModelForm
from django.urls import reverse

# Create your models here.

GRADE_CHOICES= [
    ('A+', 'A+'),
    ('A', 'A'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B', 'B'),
    ('B-', 'B-'),  
    ('C+', 'C+'),
    ('C', 'C'),
    ('C-', 'C-'),
    ('D+', 'D+'),
    ('D', 'D'),
    ('D-', 'D-'),
    ('F+', 'F+'),            
    ]

SEMESTER_CHOICES= [
    ('Fall', 'Fall'),
    ('Spring', 'Spring'),
    ('Summer Session', 'Summer Session'),
    ('J-Term', 'J-Term'),         
    ]

class Class(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField(default=0)
    semester = models.CharField(default= " ", max_length=20, choices=SEMESTER_CHOICES)
    grade = models.CharField(default= " ", max_length=3, choices=GRADE_CHOICES)
    numeric_grade = models.FloatField(default=0)
    credit_hours = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gpa:class-detail", kwargs={"id": self.id})

    @classmethod
    def cum_grades(self):
        return Class.objects.aggregate(total=Sum('numeric_grade'))['total']*Class.objects.aggregate(total=Sum('credit_hours'))['total']
    
    @classmethod
    def cum_creds(cls):
        return Class.objects.aggregate(total=Sum('credit_hours'))

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class GPA(models.Model):
    g = models.FloatField(default=0)
    @property
    def calc(self):
        return Class.cum_grades()/Class.cum_creds()['total']
    g = Class.cum_grades()/Class.cum_creds()['total']





