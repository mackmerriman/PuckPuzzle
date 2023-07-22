from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, CrontabSchedule

class Command(BaseCommand):
    help = 'Set up schedule for the daily game creation task'

    def handle(self, *args, **kwargs):
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute='0',
            hour='0',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*'
        )
        PeriodicTask.objects.get_or_create(
            crontab=schedule,
            name='Create daily game',
            task='myapp.management.commands.create_daily_game.Command'
        )
        self.stdout.write(self.style.SUCCESS('Successfully set up daily game creation schedule.'))
