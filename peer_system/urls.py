from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartingPageView.as_view(), name="starting-page"),
    path('create', views.CreatingView.as_view(), name="create"),
    path('login', views.LoginView.as_view(), name="login"),
    path('profile', views.ProfileView.as_view(), name="profile")
]
