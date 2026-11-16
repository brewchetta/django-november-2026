from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login


def home(request):
    return render(request, 'home.html')


def auth_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()      # save user to db
            login(request, user)    # login saved user
            return redirect('home')
        else:
            context = { 'form': form }
            return render(request, 'auth_signup.html', context)

    context = { 'form': SignupForm() }
    return render(request, 'auth_signup.html', context)