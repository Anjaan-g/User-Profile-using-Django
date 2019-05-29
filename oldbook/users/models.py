from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    image = models.ImageField(default='myAvatar.png',upload_to= 'profile_pics/')
    location = models.CharField(max_length = 50, null = True, blank = True)
    dob = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username.capitalize()} Profile'
