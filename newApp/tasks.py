# Create your tasks here
# from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task(name="function1")
def add(x, y):
    print("inside add 1")
    return x+y


@shared_task(name="function2")
def mul(x, y):
    return x+y


def sum(x, y):
    # to use for diff queue
    # add1.apply_async([x, y], queue='custom')
    add.delay(x, y)
    mul.delay(x, y)
    return "done"
