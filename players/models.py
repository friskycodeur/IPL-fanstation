from django.db import models
from django.urls import reverse
from django.utils import timezone


class Bowling_Stats(models.Model):
    bowling_style = models.CharField(max_length=20)
    most_wickets_in_a_match = models.IntegerField()
    economy = models.FloatField(default=0)
    five_wicket_haul = models.IntegerField(default=0)
    total_wickets = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Batting_Stats(models.Model):
    batting_style = models.CharField(max_length=20)
    total_runs = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    fifties = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Player(Batting_Stats, Bowling_Stats):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    photo = models.URLField()
    nationality = models.CharField(max_length=15)
    role_choices = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All-Rounder", "All Rounder"),
    ]
    role = models.CharField(
        max_length=12, choices=role_choices, default="Batsman"
    )
    total_matches = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("player_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
