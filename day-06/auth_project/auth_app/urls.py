from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('auth/signup', views.auth_signup, name="auth_signup"),
    path('auth/logout', views.auth_logout, name="auth_logout"),
    path('auth/login', views.auth_login, name="auth_login"),

    path('profile', views.profile, name="profile"),
    path('profile/edit', views.profile_edit, name="profile_edit"),

    path('music/create', views.music_create, name="music_create"),
    path('music/mine', views.music_mine, name="music_mine"),
    path('music/<int:id>/delete', views.music_delete, name="music_delete"),
]