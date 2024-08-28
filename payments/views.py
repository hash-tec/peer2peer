from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from  django.http import HttpResponse
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from marketplace.models import CreateListing
from user_management.models import CustomerUser
from django.db.models import Count, F,Sum


# Create your views here.

class Payment(LoginRequiredMixin, TemplateView):
    template_name = "payments/payments.html"
    def get(self, request):
         user = Cart.objects.get(user=self.request.user)
         cart_items = CartItem.objects.filter(user = user)
         total_amount = total_amount = CartItem.objects.filter(user=user).aggregate( total=Sum(F('price') * F('quantity')))
         full_name = self.request.user.get_full_name()
         username = self.request.user.username
         email = self.request.user.email
         address = self.request.user.address
         print(full_name, address)
         print(f"{email} dont know")
         return render(request, "payments/payments.html",{"fullname":full_name,
                                                          "email":email,
                                                          "address":address,
                                                          "total_amount":total_amount,
                                                          "username": username})
        # def get(self, request):
        #     user = self.request.user.fullname