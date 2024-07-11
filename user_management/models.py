from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerUser(AbstractUser):
    bio = models.TextField(max_length=250)
    dob=models.DateField()

