from django.urls import path
from .views import CartView, AddCartview

urlpatterns = [
    path('', CartView.as_view(), name ="cart"),
    path('add-cart/<int:itemid>', AddCartview.as_view(), name="addcart")
]
