from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm, LoginForm
from .models import Author, Genre, Book

User = get_user_model()


# HOME #
class HomeView(TemplateView):
    template_name = 'home.html'


# AUTH ########################################################################

# SIGNUP #
class SignupView(FormView):
    template_name = 'auth/signup.html'
    form_class = SignupForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# LOGIN #
class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            context = { 'form': form, 'error': 'Invalid username or password' }
            return render(self.request, self.template_name, context)


# LOGOUT #
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    

# AUTHOR ##############################################################################

# CREATE AUTHOR #
# the LoginRequiredMixin needs to go first to work
class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author/form.html'
    success_url = '/authors'

# LIST AUTHOR #
class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'author/list_view.html'


# GENRE ##############################################################################

# CREATE GENRE #
class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    template_name = 'genre/form.html'
    success_url = '/genres'

# LIST GENRE #
class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'genre/list_view.html'


# BOOK ##############################################################################

# CREATE BOOK #
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['genres', 'author', 'title', 'description']
    template_name = 'book/form.html'
    success_url = '/books'

# LIST BOOK #
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/list_view.html'