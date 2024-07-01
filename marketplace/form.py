from django import forms
from . import models

class CreateListingForm(forms.ModelForm):


    class Meta:
        model = models.CreateListing
        exclude = ("slug",)