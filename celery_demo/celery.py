from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from newApp.tasks import add

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo.settings')
app = Celery('celery_demo')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.task_default_queue = 'default'
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'newApp.tasks.add',
        'schedule': 5.0,   # crontab(minute='*/1')
        'args': (16, 16)
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
