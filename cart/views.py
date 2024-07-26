from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from marketplace.models import CreateListing
from cart.models import Cart, CartItem
from django.db.models import Count, F,Sum

# Create your views here.

class CartView(TemplateView):
        template_name = "cart/cart.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = Cart.objects.get(user = self.request.user)
            context["user_cart"] = CartItem.objects.filter(user = user) 
            total_amount = CartItem.objects.filter(user=user).aggregate( total=Sum(F('price') * F('quantity')))
            context["total_amount"] = total_amount
            print(total_amount)
                 
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
              print(item.item_name)
                                  
              try:
                   cart_user = Cart.objects.get(user = cur_user)
              except:
                    cart_user = Cart.objects.create(user = cur_user)
              cart_user.save()
              try:
                  filter_cart = CartItem.objects.get(user = cart_user, item_name = item.item_name, brand = item.brand)
                  filter_cart.quantity += 1
                  filter_cart.save()
              except:
                                  cart = CartItem.objects.create(item_name=item.item_name, 
                                         brand=item.brand,
                                        description=item.description, 
                                        price=item.price, 
                                        image=item.image, 
                                        user = cart_user)

             

              
            

             
              
              print(item_id + "hello")
              return render(request, "cart/addcart.html", {"item_id":item_id,
                                                        "item": item,
                                                        })
              