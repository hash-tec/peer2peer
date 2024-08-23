from django.shortcuts import render
from django.views.generic import TemplateView
from  django.http import HttpResponse
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from marketplace.models import CreateListing
from user_management.models import CustomerUser
from django.db.models import Count, F,Sum


# Create your views here.

  
