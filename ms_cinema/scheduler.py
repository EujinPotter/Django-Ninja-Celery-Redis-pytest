from celery import current_app
from datetime import datetime


def scheduler(task_name, time, args, callback):
    app = current_app._get_current_object()
    app.tasks.get(task_name)
    app.conf.beat_schedule[task_name] = {
        'task': task_name,
        'args': args
    }
