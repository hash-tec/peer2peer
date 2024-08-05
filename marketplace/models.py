from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class CreateListing(models.Model):
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="items_images", null=True)
    slug = models.SlugField(default="", null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.item_name} "
    
class Requester(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
      
class RequestItem(models.Model):
    user = models.ForeignKey(Requester, on_delete=models.CASCADE, null = True, related_name="requester")
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="items_images", null=True)
    slug = models.SlugField(default="", null=True)