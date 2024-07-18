from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

class CartView(TemplateView):
    template_name ="cart/cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        return context
    