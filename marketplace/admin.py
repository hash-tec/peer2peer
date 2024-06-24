from django.contrib import admin
from marketplace.models import CreateListing


class CreateListingAdmin(admin.ModelAdmin):
    list_display = ("item_name", "brand", "price", "date_created")
admin.site.register(CreateListing, CreateListingAdmin)
