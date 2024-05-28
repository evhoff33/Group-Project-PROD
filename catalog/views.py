from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player, Game, Division, Standings
from .forms import TeamForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from nba_api.stats.endpoints import leaguestandings
from nba_api.live.nba.endpoints import scoreboard


def landing_page(request):
    # new development for home page
    game_data = scoreboard.ScoreBoard().get_dict()['scoreboard']['games']

    recent_games = []

    for game in game_data:
        game_info = {
            'home_team': game['homeTeam']['teamName'],
            'home_score': game['homeTeam']['score'],
            'away_team': game['awayTeam']['teamName'],
            'away_score': game['awayTeam']['score'],
            'game_status': game['gameStatusText']
        }
        recent_games.append(game_info)
    # Fetch all players
    players = Player.objects.all()

    # Fetch all teams
    teams = Team.objects.all()
    for team in teams:
        just_team_name = team.name.split()
        team.name = just_team_name[-1]

    selected_player = None
    selected_team = None

    if request.method == 'POST':
        selected_player_id = request.POST.get('favorite_player')
        selected_team_id = request.POST.get('favorite_team')

        if selected_player_id:
            selected_player = Player.objects.get(id=selected_player_id)
        if selected_team_id:
            selected_team = Team.objects.get(id=selected_team_id)

    context = {
        'recent_games': recent_games,
        'players': players,
        'teams': teams,
        'selected_player': selected_player,
        'selected_team': selected_team,
    }

    return render(request, 'landing_page.html', context)


def divisions_page(request):
    divisions = Division.objects.prefetch_related('team_set').all()  # Query divisions with teams
    return render(request, 'divisions_page.html', {'divisions': divisions})

def teams_page(request):
    # Fetch all teams
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'teams_page.html', context)

def games_page(request):
    # Fetch all games
    # Fetch details of a specific game
    # Get the game data
    game_data = scoreboard.ScoreBoard().get_dict()['scoreboard']['games']

    # Extract relevant information
    recent_games_data = []
    for game in game_data:
        game_info = {
            'home_team': game['homeTeam']['teamName'],
            'home_score': game['homeTeam']['score'],
            'away_team': game['awayTeam']['teamName'],
            'away_score': game['awayTeam']['score'],
            'game_status': game['gameStatusText']
        }
        recent_games_data.append(game_info)

    games = Game.objects.all()

    context = {'recent_games': recent_games_data, 'games': games}

    return render(request, 'games_page.html', context)

def game_details_page(request, game_id):
    # Fetch details of a specific game
    game = Game.objects.get(pk=game_id)
    context = {'game': game}
    return render(request, 'game_details_page.html', context)

def players_page(request):
    # Fetch all players
    players = Player.objects.all()
    context = {'players': players}
    return render(request, 'players_page.html', context)

def standings_page(request):
    # Fetch standings for all teams
    standings_data = leaguestandings.LeagueStandings().get_dict()['resultSets'][0]['rowSet']

    # Create a list to store the standings
    standings = []

    # Initialize num count variable.
    standing_num = 1

    # Iterate over each team in the standings data
    for team in standings_data:
        team_data = {
            'team_number': standing_num, # team number to list.
            'team_city': team[3], # Team city
            'team_name': team[4],  # Team name
            'wins': team[12],  # Number of wins
            'losses': team[13],  # Number of losses
            'win_pct': team[14],  # Win percentage
            'conference': team[5],  # Conference
            'division': team[9]  # Division
        }
        standings.append(team_data)
        standing_num+=1



    context = {'standings': standings}
    return render(request, 'standings_page.html', context)



#def team_details(request, team_id):
    # Fetch details of a specific team
#    team = get_object_or_404(Team, pk=team_id)
#    context = {'team': team}
 #   return render(request, 'team_details.html', context)
 #testing some changes - 4/5/24
def team_details(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'team_details.html', {'team': team})

@staff_member_required
def edit_team_details(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_details', team_id=team_id)
    else:
        form = TeamForm(instance=team)
    return render(request, 'edit_team_details.html', {'team': team, 'form': form})

def player_details(request, player_id):
    # Fetch details of a specific player
    player = get_object_or_404(Player, pk=player_id)
    context = {'player': player}
    return render(request, 'player_details.html', context)