from django.contrib import admin
from cart.models import Cart, CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ["user", "item_name", "quantity" ]

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart)