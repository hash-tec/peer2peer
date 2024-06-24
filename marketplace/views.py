from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from user_management.models import Profile
from marketplace.models import CreateListing
from marketplace.form import CreateListingForm


# Create your views here.
class AvailableListingView(TemplateView):
    template_name = "marketplace/available-listing.html"

class CreateListingView(TemplateView):
    template_name ="marketplace/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateListingForm()
        return context
    