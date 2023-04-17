import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ms_cinema.settings")
app = Celery("ms_cinema")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
