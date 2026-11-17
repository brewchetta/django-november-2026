from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('auth/signup', views.SignupView.as_view(), name="signup_view"),
    path('auth/login', views.LoginView.as_view(), name="login_view"),
    path('auth/logout', views.LogoutView.as_view(), name="logout_view"),
]