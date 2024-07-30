from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from marketplace.models import CreateListing
from marketplace.form import CreateListingForm
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
        form = CreateListingForm(request.POST, request.FILES)
        if form.is_valid():
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
     