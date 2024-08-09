from django.contrib import admin
from cart.models import Cart, CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ["user", "item_name", "quantity", "id" ]

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart)