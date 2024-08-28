from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display =("user", "amount", "transaction_id","date_created")
admin.site.register(Payment, PaymentAdmin)