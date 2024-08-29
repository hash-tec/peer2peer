from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from cart.models import Cart, CartItem
from .models import Payment, BuyerPay
from django.db.models import F,Sum
import uuid

# Create your views here.

class PaymentView(LoginRequiredMixin, TemplateView):
    template_name = "payments/payments.html"
    def get(self, request):
         user = Cart.objects.get(user=self.request.user)
         cart_items = CartItem.objects.filter(user = user)
         total_amount = total_amount = CartItem.objects.filter(user=user).aggregate( total=Sum(F('price') * F('quantity')))
         full_name = self.request.user.get_full_name()
         username = self.request.user.username
         email = self.request.user.email
         address = self.request.user.address
         return render(request, "payments/payments.html",{"fullname":full_name,
                                                          "email":email,
                                                          "address":address,
                                                          "total_amount":total_amount,
                                                          "username": username})
        # def get(self, request):
        #     user = self.request.user.fullname

class Payment_sucessful(TemplateView):
     template_name = "payments/sucessful.html"
     def get(self, request):
         user, created = BuyerPay.objects.get_or_create(user=self.request.user)
         cart_user = Cart.objects.get(user=self.request.user)
         total_amount = CartItem.objects.filter(user=cart_user).aggregate( total=Sum(F('price') * F('quantity')))
         txref = f"FLW-{uuid.uuid4()}"
         purchased_history = Payment.objects.create(user = user,
                                                    amount = total_amount["total"],
                                                    transaction_id = txref )
         return render(request, "payments/sucessful.html", )