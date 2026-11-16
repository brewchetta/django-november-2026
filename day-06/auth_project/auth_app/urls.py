from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('auth/signup', views.auth_signup, name="auth_signup"),
]