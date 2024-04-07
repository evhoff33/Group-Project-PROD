from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('divisions/', views.divisions_page, name='divisions_page'),
    path('teams/', views.teams_page, name='teams_page'),
    path('team/<int:team_id>/', views.team_details, name='team_details'),
    path('games/', views.games_page, name='games_page'),
    path('game/<int:game_id>/', views.game_details_page, name='game_details_page'),
    path('players/', views.players_page, name='players_page'),
    path('player/<int:player_id>/', views.player_details, name='player_details'),
    path('standings/', views.standings_page, name='standings_page'),
    # Add more paths for other views as needed
]
