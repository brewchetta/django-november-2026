from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('songs/<int:id>', views.song_detail, name="song_detail"),
]