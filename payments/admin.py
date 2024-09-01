from django.contrib import admin
from .models import Payment, Purchased_products

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display =("user", "amount", "transaction_id","date_created")
admin.site.register(Payment, PaymentAdmin)

class PurchasedAdmin(admin.ModelAdmin):
    list_display = ("user", "item_name", "quantity", "price")
admin.site.register(Purchased_products, PurchasedAdmin)