from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta():
        model=Player
        fields=('name','nationality','role','batting_style','bowling_style','age','highest_score','avg','economy',)