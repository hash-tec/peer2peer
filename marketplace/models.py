from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"
    
    
class Buyer(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

        def __str__(self):
             return f"{self.user}"
class CreateListing(models.Model):
    seller = models.ForeignKey(Seller, on_delete= models.CASCADE, null=True,related_name="seller")
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=0)
    discount = models.DecimalField(max_digits=100, decimal_places=0, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=1000000000000000, decimal_places=0, null=True)
    date_created = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="items_images", null=True)
    slug = models.SlugField(default="", null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_name)
        super().save(*args, **kwargs)
    
class Requester(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"
      
class RequestItem(models.Model):
    user = models.ForeignKey(Requester, on_delete=models.CASCADE, null = True, related_name="requester")
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=0, null=True)
    date_created = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="requesteditems-image", null=True)
    slug = models.SlugField(default="", null=True)


class Buy(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name= "cart_item", null=True)
    seller = models.CharField(max_length=50, null=True)
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=0)
    discount = models.DecimalField(max_digits=100, decimal_places=0, null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=1000000000000000, decimal_places=0, null=True)
    date_created = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="items_images", null=True)

    def __str__(self):
        return f"{self.buyer} {self.item_name}"