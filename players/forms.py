from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta():
        model=Player
        fields=('name','nationality','role','batting_style','bowling_style','age','total_matches','total_runs','highest_score','best_bowling_figures','avg','economy','five_wickets','total_wickets','fifties','hundreds',)  