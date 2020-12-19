from django.db import models
from django.urls import reverse


class Player(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    nationality=models.CharField(max_length=15)
    role_choices=[('Batsman','Batsman'),('Bowler','Bowler'),('All-Rounder','All Rounder'),]
    role=models.CharField(max_length=12,choices=role_choices,default='Batsman')
    batting_style=models.CharField(max_length=20)
    bowling_style=models.CharField(max_length=20)
    #IPL stats
    total_matches=models.IntegerField(default=0)
    total_runs=models.IntegerField(default=0)
    highest_score=models.IntegerField(default=0)
    best_bowling_figures=models.CharField(max_length=7,default='R/W')
    avg=models.FloatField(default=0)
    economy=models.FloatField(default=0)
    five_wickets=models.IntegerField(default=0)
    total_wickets=models.IntegerField(default=0)
    fifties=models.IntegerField(default=0)
    hundreds=models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()    
    
    def get_absolute_url(self):
        return reverse("player_detail", kwargs={'pk': self.pk})    

    def __str__(self):
        return self.name