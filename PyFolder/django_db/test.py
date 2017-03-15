import django
from apps.leagues.models import *

django.setup()

teams = Team.objects.filter(location='Dallas')
for team in teams:
    print team.location, team.team_name
    players = team.curr_players.all()
    for player in players:
        print "\t", player.first_name, player.last_name