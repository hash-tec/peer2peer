from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from marketplace.models import CreateListing, Requester, RequestItem, Seller
from marketplace.form import CreateListingForm, RequestItemForm
from cart.models import CartItem, Cart
from django.contrib.auth.models import User


# Create your views here.
class AvailableListingView(TemplateView):
    template_name = "marketplace/available-listing.html"
    def get_context_data(self, **kwargs):
        user = Cart.objects.get(user =self.request.user)
        context = super().get_context_data(**kwargs)
        context["items_created"] = CreateListing.objects.all()
        context["cart_no"] = CartItem.objects.filter(user = user).count()
        return context
    

    

class CreateListingView(TemplateView):
    template_name ="marketplace/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateListingForm()
        return context
    
    def get(self, request):
        form = CreateListingForm()
        return render(request,"marketplace/create.html", {"form":form} )
    
    
    def post(self, request):
        user = self.request.user
        form = CreateListingForm(request.POST, request.FILES)
        seller, created = Seller.objects.get_or_create(user = user)
        if form.is_valid():
            product_name = request.POST["item_name"]
            brand = request.POST["brand"]
            discount = request.POST["discount"]
            price = request.POST["price"]
            if discount:
                calc_discount = int(discount) * int(price) // 100
                discounted_price = int(price) - calc_discount
                listing = form.save(commit=False)
                listing.discounted_price = discounted_price
                listing.seller = seller
                listing.save()
            else:
                form.save()
            return redirect('thanks')
        return render(request,"marketplace/create.html", {"form":form} )
    

    
class ItemDetailView(TemplateView):
    template_name = "marketplace/item-details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail_key = kwargs["detail"]
        context["details"] = CreateListing.objects.get(slug = detail_key)
        return context
    
class ThanksView(TemplateView):
    template_name = "marketplace/thanks.html" 
     
class RequestView(TemplateView):
    template_name="marketplace/requestform.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RequestItemForm()
        return context
    
    def post(self, request):
        user = self.request.user
        try:
            requester = Requester.objects.get(user=user)
        except:
            requester = Requester.objects.create(user = user)

        form = RequestItemForm(request.POST, request.FILES)
        product_name = request.POST["item_name"]
        brand = request.POST["brand"]
        price = request.POST["price"]
        image = request.FILES["image"]
      
        if form.is_valid():
            item_requested= RequestItem.objects.create(item_name= product_name, 
                                         brand=brand, 
                                         price=price, 
                                         image=image, 
                                         user = requester)
            
            return redirect("request")
        return render(request, "marketplace/discover.html",{"form": form})
class DiscoverView(TemplateView):
        template_name = "marketplace/discover.html"
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["requested_items"] = RequestItem.objects.all()
            return context

class OrdersView(TemplateView):
    template_name = "marketplace/orders.html"
    
    def get(self, request, *args, **kwargs):
        user = Seller.objects.get(user = self.request.user)
        orders_list = CreateListing.objects.filter(seller = user)
        return render(request, "marketplace/orders.html", {"orders": orders_list})
    
class CancelListingView(TemplateView):
        def get(self, request, *args, **kwargs):
            item_id = kwargs["itemid"]
            item = CreateListing.objects.get(id = item_id)
            item.delete()
            return redirect("orders")