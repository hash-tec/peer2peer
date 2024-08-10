from django.urls import path
from .views import CartView, AddCartview, CartAddView, CartReductionView, RemoveItem

urlpatterns = [
    path('', CartView.as_view(), name ="cart"),
    path('add-cart/<int:itemid>', AddCartview.as_view(), name="addcart"),
    path('cart-addition/<int:itemid>', CartAddView.as_view(), name="addition"),
    path('cart-reduction/<int:itemid>', CartReductionView.as_view(), name="reduction"),
    path('remove/<int:itemid>', RemoveItem.as_view(), name="remove" ),

]
