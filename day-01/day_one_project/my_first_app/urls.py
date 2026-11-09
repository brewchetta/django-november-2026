from django.urls import path

# import all views from views.py
from . import views

urlpatterns = [
    # two routes:

    # home route - "/"
    path('', views.home, name="home"),
    # about route - "/about"
    path('about', views.about, name="about"),
]