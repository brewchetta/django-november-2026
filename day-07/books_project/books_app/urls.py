from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    
    path('auth/signup', views.SignupView.as_view(), name="signup_view"),
    path('auth/login', views.LoginView.as_view(), name="login_view"),
    path('auth/logout', views.LogoutView.as_view(), name="logout_view"),

    path('authors/create', views.AuthorCreateView.as_view(), name="author_create"),
    path('authors', views.AuthorListView.as_view(), name="author_list"),

    path('genres/create', views.GenreCreateView.as_view(), name="genre_create"),
    path('genres', views.GenreListView.as_view(), name="genre_list"),

    path('books/create', views.BookCreateView.as_view(), name="book_create"),
    path('books', views.BookListView.as_view(), name="book_list"),
]