from django.urls import path
from . import views


urlpatterns = [
    path('', views.AvailableListingView.as_view(), name="available-listing"),
    path('create/', views.CreateListingView.as_view(), name="create"),
    path('thanks/', views.ThanksView.as_view(), name="thanks")
]
