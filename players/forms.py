from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta():
        model=Player
        fields=('name','nationality','role','batting_style','bowling_style','age','test_matches','test_runs','test_highest_score','test_best_bowling_figures','test_avg','test_economy','test_wickets','test_five_wickets','test_fifties','test_hundreds','odi_matches','odi_runs','odi_highest_score','odi_best_bowling_figures','odi_avg','odi_economy','odi_wickets','odi_five_wickets','odi_fifties','odi_hundreds','t20_matches','t20_runs','t20_highest_score','t20_best_bowling_figures','t20_avg','t20_economy','t20_wickets','t20_five_wickets','t20_fifties','t20_hundreds')
        