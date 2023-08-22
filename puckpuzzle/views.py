import os
import random
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils import timezone
from django.db.models import Q
from .models import Players, DailyGame
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def run_daily_game_creation(request):
    # Ensure the request is from App Engine Cron
    if 'HTTP_X_APPENGINE_CRON' not in request.headers:
        return HttpResponse('Unauthorized', status=403)

    # Call the management command
    call_command('create_daily_game')

    return HttpResponse('Task executed')


# ...
def index(request):
    today = timezone.now().date()
    game = DailyGame.objects.get(date=today)
    return render(request, 'puckpuzzle/index.html', {'teams': game.teams})


def filterPlayers(request):
    if request.method == 'GET':
        name = request.GET['q']

        players = list(Players.objects.filter(
            Q(first__startswith=name) | Q(last__startswith=name) | Q(player__startswith=name)).values())

        return JsonResponse(players, safe=False)
    else:
        return HttpResponse("Request method is not a GET")


def checkPlayer(request):
    if request.method == 'GET':
        guess = request.GET['player']
        row = request.GET['row'].lower().replace(' ', '_')
        col = request.GET['col'].lower().replace(' ', '_')
        check = Players.objects.get(pk=guess)

        if getattr(check, row) == 0:
            return JsonResponse({'result': False})

        if getattr(check, col) == 0:
            return JsonResponse({'result': False})

        return JsonResponse({'result': True})
