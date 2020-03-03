from django.contrib import admin

from .models import Class, GPA

class ChoiceInline(admin.TabularInline):
    model = Class
    extra = 3

admin.site.register(Class)
admin.site.register(GPA)