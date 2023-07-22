from django.core.management.base import BaseCommand
from django.utils import timezone
from puckpuzzle.models import DailyGame
import os
import random


class Command(BaseCommand):
    help = 'Create a new daily game'

    def handle(self, *args, **kwargs):
        teams_dir = os.path.join(os.path.dirname(
            __file__), '../../static/puckpuzzle/images/logos')
        teams = [f.split('.')[0] for f in os.listdir(teams_dir)
                 if os.path.isfile(os.path.join(teams_dir, f))]
        selected_teams = random.sample(teams, 6)

        game = DailyGame(date=timezone.now().date(), teams=selected_teams)
        game.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully created game for date "%s"' % game.date))
