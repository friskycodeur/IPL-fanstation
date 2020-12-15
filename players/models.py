from django.db import models
from django.urls import reverse


class Player(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    nationality=models.CharField(max_length=15)
    role_choices=[('Bat','Batsman'),('Bowl','Bowler'),('Field','Fielder'),]
    role=models.CharField(max_length=7,choices=role_choices,default='Bat')
    batting_style=models.CharField(max_length=20)
    bowling_style=models.CharField(max_length=20)
    # Test stats
    test_matches=models.IntegerField(default=0)
    test_runs=models.IntegerField(default=0)
    test_highest_score=models.IntegerField(default=0)
    test_best_bowling_figures=models.CharField(max_length=7,default='R/W')
    test_avg=models.FloatField(default=0)
    test_economy=models.FloatField(default=0)
    test_wickets=models.IntegerField(default=0)
    test_five_wickets=models.IntegerField(default=0)
    test_fifties=models.IntegerField(default=0)
    test_hundreds=models.IntegerField(default=0)
    # ODI stats
    odi_matches=models.IntegerField(default=0)
    odi_runs=models.IntegerField(default=0)
    odi_highest_score=models.IntegerField(default=0)
    odi_best_bowling_figures=models.CharField(max_length=7,default='R/W')
    odi_avg=models.FloatField(default=0)
    odi_economy=models.FloatField(default=0)
    odi_wickets=models.IntegerField(default=0)
    odi_five_wickets=models.IntegerField(default=0)
    odi_fifties=models.IntegerField(default=0)
    odi_hundreds=models.IntegerField(default=0)
    #t20 stats
    t20_matches=models.IntegerField(default=0)
    t20_runs=models.IntegerField(default=0)
    t20_highest_score=models.IntegerField(default=0)
    t20_best_bowling_figures=models.CharField(max_length=7,default='R/W')
    t20_avg=models.FloatField(default=0)
    t20_economy=models.FloatField(default=0)
    t20_five_wickets=models.IntegerField(default=0)
    t20_wickets=models.IntegerField(default=0)
    t20_fifties=models.IntegerField(default=0)
    t20_hundreds=models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()    
    
    def get_absolute_url(self):
        return reverse("player_detail", kwargs={'pk': self.pk})    

    def __str__(self):
        return self.name