from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_photo=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username


