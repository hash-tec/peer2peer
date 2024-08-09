from django.urls import path
from .views import CartView, AddCartview, CartAddView, CartRemoveView

urlpatterns = [
    path('', CartView.as_view(), name ="cart"),
    path('add-cart/<int:itemid>', AddCartview.as_view(), name="addcart"),
    path('cart-addition/<int:itemid>', CartAddView.as_view(), name="addition"),
    path('cart-remove/<int:itemid>', CartRemoveView.as_view(), name="remove")

]
