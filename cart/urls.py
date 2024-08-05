from django.urls import path
from .views import CartView, AddCartview, CartAddView

urlpatterns = [
    path('', CartView.as_view(), name ="cart"),
    path('add-cart/<int:itemid>', AddCartview.as_view(), name="addcart"),
    path('cartaddition/<int:itemid>', CartAddView.as_view(), name="addition")
]
