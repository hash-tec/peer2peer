from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Buyer(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

        def __str__(self):
             return f"{self.user}"
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
