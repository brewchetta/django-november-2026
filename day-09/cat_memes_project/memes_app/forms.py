from django import forms
from .models import CatMeme

class CatMemeForm(forms.ModelForm):
    class Meta:
        model = CatMeme
        fields = '__all__'