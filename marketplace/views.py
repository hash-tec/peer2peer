from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from user_management.models import Profile
from marketplace.models import CreateListing
from marketplace.form import CreateListingForm


# Create your views here.
class AvailableListingView(TemplateView):
    template_name = "marketplace/available-listing.html"

    

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
        form = CreateListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        return render(request,"marketplace/create.html", {"form":form} )
class ThanksView(TemplateView):
    template_name = "marketplace/thanks.html"
    