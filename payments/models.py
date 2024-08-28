from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class BuyerPay(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

class Payment(models.Model):
    user = models.ForeignKey(BuyerPay, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
         f"{self.buyer} {self.price}"