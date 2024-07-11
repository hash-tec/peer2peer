from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect



# Create your views here.
class StartingPageView(TemplateView):
    template_name = "user_management/starting-page.html"

    

class SignUpView(TemplateView):
    template_name = "user_management/signup.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = "hi"
        return context
    

class LoginView(TemplateView):
    template_name = "user_management/login.html"

class ProfileView(TemplateView):
    template_name = "user_management/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = "hi"
        return context
    
    
class AccountView(TemplateView):
    template_name = "user_management/account.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = kwargs['username']
        context["profile"] = "hi"
        return context
    
