from django.urls import path
from . import views


urlpatterns = [
    path('', views.AvailableListingView.as_view(), name="available-listing")
]
