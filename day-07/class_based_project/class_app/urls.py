from django.urls import path
from . import views

urlpatterns = [
    # always call class based views with .as_view()
    path('', views.HomeView.as_view(), name="home"),
    path('about', views.AboutView.as_view(), name="about"),

    path('videogames', views.VideogameListView.as_view(), name="videogames_list"),
    path('videogames/create', views.VideogameCreateView.as_view(), name="videogames_create"),
    path('videogames/<int:id>/edit', views.VideogameEditView.as_view(), name="videogames_edit"),

    path('movies', views.MovieListView.as_view(), name="movies_list"),
    path('movies/<int:pk>', views.MovieDetailView.as_view(), name="movie_detail"),
    path('movies/create', views.MovieCreateView.as_view(), name="movies_create"),
    path('movies/<int:pk>/edit', views.MovieEditView.as_view(), name="movies_edit"),
]