from django.urls import path
from . import views

urlpatterns = [
    # always call class based views with .as_view()
    path('', views.HomeView.as_view(), name="home"),
    path('about', views.AboutView.as_view(), name="about"),

    path('videogames', views.VideogameListView.as_view(), name="videogames_list"),
    path('videogames/create', views.VideogameCreateView.as_view(), name="videogames_create"),
    path('videogames/<int:id>/edit', views.VideogameEditView.as_view(), name="videogames_edit"),
]