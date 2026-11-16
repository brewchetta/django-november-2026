from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, LoginForm, MusicForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Music
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


# AUTHENTICATION #################
# checking that a user is who they say they are
# using usernames and passwords
##################################

# AUTHORIZATION #################
# checking that a user has privileges to do and 
# be where they are
##################################


# SIGNUP ########################
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


# LOGIN  #######################
def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # check that the username & password match in the db
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        # if invalid form or invalid authentication
        context = { 'form': form, 'error': "Invalid username or password, please try again" }
        return render(request, 'auth_login.html', context)

    context = { 'form': LoginForm() }
    return render(request, 'auth_login.html', context)


# LOGOUT #######################
@login_required
def auth_logout(request):
    logout(request)
    return redirect('home')


# PROFILE #######################
@login_required # ensures that profile is only for logged in users
def profile(request):
    return render(request, 'profile.html')


# PROFILE EDIT###################
@login_required
def profile_edit(request):
    current_user = request.user
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=current_user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            context = { 'form': form }
            return render(request, 'profile_edit.html', context)

    form = ProfileForm(instance=current_user.profile)
    context = { 'form': form }
    return render(request, 'profile_edit.html', context)



# MUSIC CREATE ##################
@login_required
def music_create(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            new_music = form.save()
            new_music.user = request.user
            new_music.save() # registers the user as the submitter of the music
            return redirect('home')
        else:
            context = { 'form': form }
            return render(request, 'music_create.html', context) 

    context = { 'form': MusicForm() }
    return render(request, 'music_create.html', context)


# MUSIC MINE  ##################
@login_required
def music_mine(request):
    my_music = request.user.submitted_music.all()
    context = { 'my_music': my_music }
    return render(request, 'music_mine.html', context)


# MUSIC DELETE #################
@login_required
def music_delete(request, id):
    music = get_object_or_404(Music, id=id)
    current_user = request.user

    if music.user == current_user: # if authorized, delete and rerender/redirect
        music.delete()
        return redirect('music_mine')

    else: # if users don't match we show the user they are not authorized...
        return HttpResponse("Unauthorized to delete that...", status=401)