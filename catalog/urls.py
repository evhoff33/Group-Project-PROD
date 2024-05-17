from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


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
    #path('recent-games/', views.recent_games, name='recent_games'),
    # forgot password - reset
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # IMPORTANT – THE URL BELOW MUST BE AFTER THE PASSWORD RESET CUSTOM FORM
    # ABOVE if included- was in front of the reset password
    # bringing up the django version first
    # path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # Add more paths for other views as needed
]
