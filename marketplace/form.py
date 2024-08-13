from django import forms
from . import models

class CreateListingForm(forms.ModelForm):


    class Meta:
        model = models.CreateListing
        labels = {
            "first_name": "First Name",
            "last_name":"Last name",
            "username":"Username",
            "password":"Password"
        }
        exclude = ("slug","discounted_price", "seller")

class RequestItemForm(forms.ModelForm):

    class Meta:
        model = models.RequestItem
        labels={
            "item_name":"Product Name",
            "brand": "Product Brand",
            "price": "Price willing to pay",
        }

        exclude =("slug","user", )