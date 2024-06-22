from django.contrib import admin
from . import models
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

admin.site.register(models.Profile, ProfileAdmin)