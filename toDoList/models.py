from django.db import models

# Create your models here.
class toDoList(models.Model):
    list_text = models.CharField(max_length=200)
    