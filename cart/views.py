from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from marketplace.models import CreateListing
from cart.models import Cart, CartItem

# Create your views here.

class CartView(TemplateView):
        template_name = "cart/cart.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = Cart.objects.get(user = self.request.user)
            context["user_cart"] = CartItem.objects.filter(user = user)
            return context
        
    
class AddCartview(TemplateView):
        template_name = "cart/addcart.html"
        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     item_id = kwargs["itemid"]
        #     context["get_item"] = CreateListing.objects.get(id = item_id)
        #     return context
        def post(self, request, *args, **kwargs):
              cur_user = self.request.user
              item_id = request.POST["item_id"]
              item = CreateListing.objects.get(id = item_id)
              cart_user = Cart.objects.get(user = cur_user)
            

             
              cart = CartItem.objects.create(item_name=item.item_name, 
                                         brand=item.brand,
                                        description=item.description, 
                                        price=item.price, 
                                        image=item.image, 
                                        user = cart_user)
              
              print(cart.quantity)
              cart.quantity =+ 1
              cart.save()
              print(cart.quantity)

             
              
              print(item_id + "hello")
              return render(request, "cart/addcart.html", {"item_id":item_id,
                                                        "item": item,
                                                        })
              