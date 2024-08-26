from django.shortcuts import render
from django.views.generic import TemplateView
from  django.http import HttpResponse
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from marketplace.models import CreateListing
from user_management.models import CustomerUser
from django.db.models import Count, F,Sum


# Create your views here.

  
class Payment(TemplateView):
    template_name = "payments/payments.html"
    def get(self, request):
         full_name = self.request.user.get_full_name()
         print(full_name)
         return render(request, "payments/payments.html")
        # def get(self, request):
        #     user = self.request.user.fullname