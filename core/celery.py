import os

from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

app = Celery('apps.atendance')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    create_attendance.delay(1)
