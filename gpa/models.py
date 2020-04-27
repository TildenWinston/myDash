from django.db import models
from django.forms import ModelForm
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth import get_user_model

year = datetime.datetime.today().year
YEARS = [year - i for i in range(8)]
YEAR_CHOICES = []
for y in YEARS:
    YEAR_CHOICES.append((y,y))

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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField(choices=YEAR_CHOICES)
    semester = models.CharField(default= " ", max_length=20, choices=SEMESTER_CHOICES)
    grade = models.CharField(default= " ", max_length=3, choices=GRADE_CHOICES)
    numeric_grade = models.FloatField(default=0.0)
    credit_hours = models.FloatField(default=0, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gpa:class-list")
    
    @property
    def grade_weight(self):
        return self.credit_hours * self.numeric_grade

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'





