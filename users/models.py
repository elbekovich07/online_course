from django.db import models

from courses.models import User


# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=120,null=True)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=120,null=False, unique=True)
    email = models.CharField(max_length=120,null=False, unique=True)

