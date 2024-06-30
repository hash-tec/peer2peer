from django.db import models
from django.utils.text import slugify


# Create your models here.
class CreateListing(models.Model):
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="items_images", null=True)
    slug = models.SlugField(default="", null=True)
    def __str__(self):
        return f"{self.item_name} "