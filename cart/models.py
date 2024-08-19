from django.db import models
from django.contrib.auth.models import User
from marketplace.models import CreateListing
from django.conf import settings


# Create your models here.

class Cart(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

        def __str__(self):
             return f"{self.user}"
class CartItem(models.Model):
    user = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name= "cart_item", null=True)
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.FileField(upload_to="items_images", null=True)


    def __str__(self):
        return f"{self.item_name} {self.quantity}"
 