from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from .form import ProfileForm
from.models import Profile


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
        context["profiles"] = Profile.objects.all()
        return context
    
    
class AccountView(TemplateView):
    template_name = "peer_system/account.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = kwargs['username']
        context["profile"] = Profile.objects.get(username = profile_id)
        return context
    
