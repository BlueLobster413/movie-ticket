# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import film

# create a ModelForm
class filmForm(forms.ModelForm):
    class Meta:
        model = film
        fields = [
            "movie_name",
            "movie_lang"
            ]
        labels = {
            "movie_name":"Film Name",
            "movie_lang":"Language",
        }
        
