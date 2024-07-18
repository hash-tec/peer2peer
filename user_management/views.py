from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from .form import SignupForm, LoginForm, ProfileForm
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
    

class HomepageView(TemplateView):
    template_name ="user_management/homepage.html"
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
                return redirect("homepage")
class ProfileView(TemplateView):
    template_name = "user_management/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profileform"] = ProfileForm(instance= self.request.user)
        context["verify_user"] = kwargs["username"]
        context["username"] = self.request.user.username
        context["firstname"] = self.request.user.first_name
        context["lastname"] = self.request.user.last_name
        context["email"] = self.request.user.email
        context["dob"] = self.request.user.dob
        context["bio"] = self.request.user.bio
        context["pfp"] = self.request.user.pfp
        return context
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        username = kwargs.get('username')
        if form.is_valid():
            form.save()
        return redirect('profile', username = username)


class AccountView(TemplateView):
    template_name = "user_management/account.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_id = kwargs['username']
        context["profile"] = "hi"
        return context
    
class ThanksView(TemplateView):
    template_name = "user_management/thanks.html"

def signout(request):
    logout(request)
    return redirect("login")