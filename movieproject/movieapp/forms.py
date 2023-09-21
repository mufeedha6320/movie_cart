from django import forms
from .models import table_movie


class Movie_form(forms.ModelForm):
    class Meta:
        model = table_movie
        fields = ['name', 'desc', 'year', 'img']
