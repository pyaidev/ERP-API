import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")
from celery.schedules import crontab

app = Celery("core")


app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'multiply-task-crontab': {
        'task': 'create_attendance',
        'schedule': crontab(hour=13, minute=18)
    },
}

