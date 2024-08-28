from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from marketplace.models import CreateListing
from cart.models import Cart, CartItem
from django.db.models import Count, F,Sum

# Create your views here.

class CartView(LoginRequiredMixin, TemplateView):
        template_name = "cart/cart.html"
        #The line of code below get the instance of the the current user from the 'Cart' model 
        # The 'user_cart' variable is to filter out the instances with the current logged in user, with this way the template will only...
        #... render cart items that belongs to the current looged in user.
        # The 'total_amount' variable use the Sum object to sum up price the quantity of each item to get the total amount of user cart
        def get(self, request, *args, **kwargs):
               user, created                           = Cart.objects.get_or_create(user = self.request.user)
               user_cart = CartItem.objects.filter(user = user) 
               total_amount = CartItem.objects.filter(user=user).aggregate( total=Sum(F('price') * F('quantity')))
               unavailable_items = []

               for cart in user_cart:
                     if not CreateListing.objects.filter(item_name=cart.item_name).exists():
                             unavailable_items.append(cart.item_name)  

              
               return render(request, "cart/cart.html", {
               "total_amount": total_amount,
               "user_cart": user_cart,
               "unavailable_items": unavailable_items
               })
                             
        
class AddCartview(LoginRequiredMixin, TemplateView): 
        def post(self, request, *args, **kwargs):
              cur_user = self.request.user
              item_id = request.POST ["item_id"]
              item = CreateListing.objects.get(id = item_id)

              # The line of code below create a new Cart instance variable from the 'cur_user' for the current user logged in
              # The Try block get the user if there is an existing instance with the  'cur_user
              # The except block create a new instance if the instance has not been created     
              try:
                   cart_user = Cart.objects.get(user = cur_user)
              except:
                    cart_user = Cart.objects.create(user = cur_user)
              cart_user.save()
              # The block of line below add an item to the user's cart into the "CartItem" model
              # The try block check the CartItem model for an existing instance with similar the newly added item to increase the quantity
              # The except block create a new insatnce if does not have a similar insttance in the model
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

              return redirect('available-listing')
              

class CartAddView(LoginRequiredMixin, TemplateView):
          template_name = "cart/addcart.html"
          def get(self, request, *args, **kwargs):
              cur_user = Cart.objects.get(user=self.request.user)
              item_id = kwargs["itemid"]
              item = CartItem.objects.get(id = item_id)
              filter_cart = CartItem.objects.get(user = cur_user, item_name = item.item_name, brand = item.brand)
              filter_cart.quantity += 1
              filter_cart.save()
              return redirect('cart')
          

class CartReductionView(LoginRequiredMixin, TemplateView):
       def get(self, request, *args, **kwargs):
              cur_user = Cart.objects.get(user=self.request.user)
              item_id = kwargs["itemid"]
              item = CartItem.objects.get(id = item_id)
              filter_cart = CartItem.objects.get(user = cur_user, item_name = item.item_name, brand = item.brand)
              filter_cart.quantity -= 1
              filter_cart.save()
              if filter_cart.quantity < 1:
                     return redirect("remove", itemid=item_id)
              return redirect('cart')
          
            

class RemoveItem(LoginRequiredMixin, TemplateView):
       def get(self, request, *args, **kwargs):
              item_id = kwargs["itemid"]
              item = CartItem.objects.get(id = item_id)
              item.delete()
              return redirect("cart")