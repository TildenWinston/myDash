from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=30)
    numeric_grade = models.FloatField(default=0)
    def __str__(self):
        return self.name