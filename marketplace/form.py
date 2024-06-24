from django import forms
from . import models

class CreateListingForm(forms.ModelForm):


    class Meta:
        model = models.CreateListing
        fields = "__all__"