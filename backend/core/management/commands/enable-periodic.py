from django.conf import settings
from django.core.management.base import BaseCommand

from django_q.models import Schedule


class Command(BaseCommand):
    help = 'Enables settings.PERIODIC_TASKS.'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        enabled_tasks = list()
        for i, (name, func, cron) in enumerate(settings.PERIODIC_TASKS):
            if Schedule.objects.filter(name=name).exists():
                continue

            s = Schedule(
                name=name, func=func, schedule_type=Schedule.CRON, cron=cron,
                kwargs={'q_options': {'task_name': 'Periodic'}}
            )
            s.next_run = s.calculate_next_run()
            s.full_clean()
            s.save()
            enabled_tasks.append(name)
        if enabled_tasks:
            self.stdout.write(f"Enabled periodic tasks: [{', '.join(enabled_tasks)}]")
        else:
            self.stdout.write("There are no periodic tasks to enable")
