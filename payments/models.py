from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class BuyerPay(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

        def __str__(self):
                return f"{self.user}"

class Payment(models.Model):
    user = models.ForeignKey(BuyerPay, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

class Purchased_products(models.Model):
    user = models.ForeignKey(BuyerPay, on_delete=models.CASCADE, related_name= "cart_item", null=True)
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.FileField(upload_to="items_images", null=True)
