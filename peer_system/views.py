from django.shortcuts import render
from django.views.generic.base import TemplateView
from .form import ProfileForm


# Create your views here.
class StartingPageView(TemplateView):
    template_name = "peer_system/starting-page.html"

class CreatingView(TemplateView):
    template_name = "peer_system/create.html"

class LoginView(TemplateView):
    template_name = "peer_system/login.html"

class ProfileView(TemplateView):
    template_name = "peer_system/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = ProfileForm
        return context
    
