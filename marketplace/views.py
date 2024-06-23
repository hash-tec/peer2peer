from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from user_management.models import Profile


# Create your views here.
class AvailableListingView(TemplateView):
    template_name = "marketplace/available-listing.html"

class CreateListingView(TemplateView):
    template_name ="marketplace/create.html"