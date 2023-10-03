from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    bio = models.CharField(max_length= 800, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='female')
    profile_picture = models.ImageField(default='users/default_profile_photo.svg', upload_to='users/%Y/%m/%d/')
