from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # MOVIE VIEWS #
    path('movies/create-new-movie', views.movie_create, name="movie_create"),
    path('movies/<slug:title_slug>', views.movie_detail, name="movie_detail"),
    path('movies/<slug:title_slug>/edit', views.movie_edit, name="movie_edit"),
    path('movies/<slug:title_slug>/delete', views.movie_delete, name="movie_delete"),

    # CHARACTER VIEWS #
    path('characters/create', views.character_create, name="character_create"),
    path('characters/<int:id>/edit', views.character_edit, name="character_edit"),
    path('characters/<int:id>/delete', views.character_delete, name="character_delete"),
]