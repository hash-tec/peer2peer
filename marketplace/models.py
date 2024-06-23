from django.db import models


# Create your models here.
class CreateListing(models.Model):
    item_name = models.CharField(max_length=150, blank=False)
    brand = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    price = models.IntegerField("")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name}"