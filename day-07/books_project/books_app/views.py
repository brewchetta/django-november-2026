from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth import get_user_model, login, logout, authenticate
from .forms import SignupForm, LoginForm

User = get_user_model()


# HOME #
class HomeView(TemplateView):
    template_name = 'home.html'


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