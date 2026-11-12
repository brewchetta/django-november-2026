from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('movies/create-new-movie', views.movie_create, name="movie_create"),
    path('movies/<slug:title_slug>', views.movie_detail, name="movie_detail"),
    path('movies/<slug:title_slug>/edit', views.movie_edit, name="movie_edit"),
    path('movies/<slug:title_slug>/delete', views.movie_delete, name="movie_delete"),
]