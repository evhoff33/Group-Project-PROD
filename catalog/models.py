from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


class Division(models.Model):
    name = models.CharField(max_length=100)

    # will want to iron out the exact fields

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='team_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this team."""
        return reverse('team_details', args=[str(self.id)])

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey('Team', related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey('Team', related_name='away_games', on_delete=models.CASCADE)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    # Need to iron out what fields to show

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"




class Standings(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    # Other fields as needed

    def __str__(self):
        return f"{self.team}: {self.wins}-{self.losses}"

from django.db import models

# Create your models here.