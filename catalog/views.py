from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player, Game, Division, Standings
from .forms import TeamForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse


def landing_page(request):
    # Fetch the three most recent games
    recent_games = Game.objects.order_by('-date')[:10]
    context = {'recent_games': recent_games}
    return render(request, 'landing_page.html', context)

#def divisions_page(request):
    # Fetch all divisions and teams
#    divisions = Division.objects.all()
#    context = {'divisions': divisions}
#    return render(request, 'divisions_page.html', context)
#testing some changes 4/5/24
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
    games = Game.objects.all()
    context = {'games': games}
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
    standings = Standings.objects.all()
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