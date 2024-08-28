from django.urls import path
from . import views
urlpatterns = [
    path("", views.PaymentView.as_view(), name = "payment"),
    path("payment-sucessful/", views.Payment_sucessful.as_view(), name = "Payment_sucessful")
 ]
 