from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField( upload_to = 'image/',null = True, blank = True)
    def __str__(self):
        return self.email
