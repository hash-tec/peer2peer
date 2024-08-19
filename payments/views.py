from django.shortcuts import render
from django.views.generic import TemplateView
from  django.http import HttpResponse
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from payments.models import Buy, Buyer

# Create your views here.
class payment(TemplateView):
    template_engine = "payments/payments.html"
    def get(self, request):
       buyer, created = Buyer.objects.get_or_create(user = self.request.user)
       user = Cart.objects.get(user = self.request.user)
       cart_items = CartItem.objects.filter(user = user)
       for item in cart_items:
           Buy.objects.create(item_name=item.item_name, 
                                         brand=item.brand,
                                         description=item.description, 
                                         price=item.price, 
                                         image=item.image, 
                                         buyer = buyer
                                         )

        
       return render(request, "payments/payments.html")