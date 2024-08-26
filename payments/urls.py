from django.urls import path
from . import views
urlpatterns = [
    path("", views.Payment.as_view(), name = "payment"),
 ]
 