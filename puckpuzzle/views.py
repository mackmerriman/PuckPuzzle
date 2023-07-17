import os
import random
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Players

# from .models import Question EXAMPLE


# ...
def index(request):
    teams_dir = os.path.join(os.path.dirname(
        __file__), './static/puckpuzzle/images/logos')
    teams = [f.split('.')[0] for f in os.listdir(teams_dir)
             if os.path.isfile(os.path.join(teams_dir, f))]
    selected_teams = random.sample(teams, 6)
    return render(request, 'puckpuzzle/index.html', {'teams': selected_teams})


def filterPlayers(request):
    if request.method == 'GET':
        name = request.GET['q']
        players = list(Players.objects.filter(
            player__startswith=name).values_list("player", flat=True))
        return JsonResponse(players, safe=False)
    else:
        return HttpResponse("Request method is not a GET")


def checkPlayer(request):
    if request.method == 'GET':
        player = request.GET['player']
        row = request.GET['row'].lower().replace(' ', '_')
        col = request.GET['col'].lower().replace(' ', '_')
        check = Players.objects.get(pk=player)

        print(row)
        print(col)
        print(getattr(check, row))
        print(getattr(check, col))

        if getattr(check, row) == 0:
            return JsonResponse({'result': False})

        if getattr(check, col) == 0:
            return JsonResponse({'result': False})

        return JsonResponse({'result': True})
