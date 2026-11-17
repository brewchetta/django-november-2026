from django import forms
from .models import VideoGame, Movie


class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = '__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'