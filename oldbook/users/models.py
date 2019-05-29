from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # image = models.ImageField( upload_to = 'image/',null = True, blank = True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    image = models.ImageField(default='myAvatar.png',upload_to= 'profile_pics/')

    def __str__(self):
        return f'{self.user.username.capitalize()} Profile'
