from django.urls import path
from . import views
urlpatterns = [
    path("", views.PaymentView.as_view(), name = "payment"),
    path("payment-sucessful/", views.PaymentSucessfulView.as_view(), name = "Payment_sucessful"),
    path("payment-history/", views.PaymentHistoryView.as_view(), name = "payment-history")
 ]
 