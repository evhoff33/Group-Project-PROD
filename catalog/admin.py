from django.contrib import admin
from .models import Team, Player, Game, Division, Standings, PlayerStat, TeamStat

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Division)
admin.site.register(Standings)
admin.site.register(PlayerStat)
admin.site.register(TeamStat)

