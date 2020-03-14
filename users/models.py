from django.db import models
from weather.models import Zipcode

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    Zipcode