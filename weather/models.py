from django.db import models
# from users.models import CustomUser
from django.contrib.auth import get_user_model

class City(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

class Zipcode(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    zip = models.CharField(max_length=5)

    def __str__(self): #show the actual city name on the dashboard
        return self.zip

    def getzip():
        return self.zip

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'Zip Codes'