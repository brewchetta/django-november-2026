from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Music, Profile

User = get_user_model() # this will import the User model from the django code


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # password1 / password2 is password confirmation


# we use a basic form for login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'favorite_artist']


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'artist']