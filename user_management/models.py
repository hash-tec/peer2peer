from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=10, null= True)
    location = models.CharField(max_length=30, null=True)
    bio_description = models.TextField()

    def __str__(self) :
        return f"{self.first_name} {self.last_name} {self.bio_description}"