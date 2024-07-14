from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartingPageView.as_view(), name="starting-page"),
    path('sign-up', views.SignUpView.as_view(), name="sign-up"),
    path('login', views.LoginView.as_view(), name="login"),
    path('profile/<str:username>', views.ProfileView.as_view(), name="profile"),
    path('thank-you', views.ThanksView.as_view(), name="thanks")

]
