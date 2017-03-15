import django
from apps.leagues.models import *
django.setup()

def first():
    leagues = League.objects.filter(sport__in=('Baseball', 'Soccer')) 
    for l in leagues:
        print "=", l.name
        teams = l.teams.exclude(location='Dallas').exclude(location='DC')
        for team in teams:
            print "\t>", team.location, team.team_name
            for player in team.curr_players.all():
                print "\t\t-", player.first_name, player.last_name

def second():
    kings = Player.objects.filter(last_name='King')
    for k in kings:
        print k.first_name, k.last_name
        for team in k.all_teams.all():
            print "\t", team.location, team.team_name

def third():
    teams = Team.objects.filter(all_players__last_name='King')
    for team in teams:
        print team.location, team.team_name
        for player in team.all_players.all():
            print "\t", player.first_name, player.last_name
