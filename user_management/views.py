from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from .form import SignupForm, LoginForm
from .models import CustomerUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
class StartingPageView(TemplateView):
    template_name = "user_management/starting-page.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context
    

    

class SignUpView(TemplateView):
    template_name = "user_management/signup.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SignupForm() 
        return context
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, "user_management/signup.html", {'form': form})

class LoginView(TemplateView):
    template_name = "user_management/login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm() 
        return context
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password']
            user = authenticate(request=request, username = username, password=password)
            if user:
                login(request, user)
                return redirect("/thank-you")
class ProfileView(TemplateView):
    template_name = "user_management/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        context["lastname"] = self.request.user.last_name
        context["email"] = self.request.user.email
        return context
    

    
class AccountView(TemplateView):
    template_name = "user_management/account.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = kwargs['username']
        context["profile"] = "hi"
        return context
    
class ThanksView(TemplateView):
    template_name = "user_management/thanks.html"