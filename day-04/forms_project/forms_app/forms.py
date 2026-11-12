from django import forms
from .models import Movie

# class MovieForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     title_slug = forms.SlugField()
#     runtime_in_minutes = forms.IntegerField()
#     director = forms.CharField(max_length=100)
#     release_date = forms.DateField()

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie

        # SYNTAX FOR ALL FIELDS
        # fields = '__all__'

        # SYNTAX FOR INDIVIDUAL FIELDS
        fields = ['title', 'title_slug', 'runtime_in_minutes', 'director', 'release_date']