from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from newApp.tasks import add1

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo.settings')
app = Celery('celery_demo')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.task_default_queue = 'default'


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# periodic task
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    #  call add1 periodically
    sender.add_periodic_task(crontab(minute='*/1'),
                             add1.s(1, 2),
                             name='prints hello every ',)
