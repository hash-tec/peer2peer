from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from cart.models import Cart, CartItem
from .models import Payment, BuyerPay, Purchased_products
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

class PaymentSucessfulView(TemplateView):
     template_name = "payments/sucessful.html"
     def get(self, request):
         user, created = BuyerPay.objects.get_or_create(user=self.request.user)
         cart_user = Cart.objects.get(user=self.request.user)
         purchased_item= CartItem.objects.filter(user=cart_user)
         total_amount = CartItem.objects.filter(user=cart_user).aggregate( total=Sum(F('price') * F('quantity')))
         txref = f"FLW-{uuid.uuid4()}"
         for item in purchased_item:
               Purchased_products.objects.create(user = user,
                                                 item_name = item.price,
                                                 brand = item.brand,
                                                 description = item.description,
                                                 price = item.price,
                                                 quantity = item.quantity,
                                                 image = item.image
                    
               )
       
         purchased_history = Payment.objects.create(user = user,
                                                    amount = total_amount["total"],
                                                    transaction_id = txref )
         delete_cart = CartItem.objects.filter(user = cart_user).delete()
         print(purchased_history.user)
         return render(request, "payments/sucessful.html", )
     
class PaymentHistoryView(TemplateView):
     template_name = "payments/history.html"
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         user = BuyerPay.objects.get(user = self.request.user)
         context["txref"] = Payment.objects.filter(user = user)
         return context
     