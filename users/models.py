from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    
    """ email = models.EmailField(('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email """