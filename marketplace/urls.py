from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.AvailableListingView.as_view(), name="available-listing"),
    path('create/', views.CreateListingView.as_view(), name="create"),
    path('items/<slug:detail>', views.ItemDetailView.as_view(), name="item-details"),
    path('thanks/', views.ThanksView.as_view(), name="thanks"),
    path('request/', views.RequestView.as_view(), name="request"),
    path('discover/', views.DiscoverView.as_view(), name="discover")
]
