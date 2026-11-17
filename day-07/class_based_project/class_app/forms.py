from django import forms
from .models import VideoGame


class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = '__all__'