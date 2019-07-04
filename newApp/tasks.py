from celery import shared_task


@shared_task(name="function1")
def add1(x, y):
    print("inside add 1")
    return x+y


@shared_task(name="function2")
def add2(x, y):
    return x+y


def sum(x, y):
    # to use for diff queue
    # add1.apply_async([x, y], queue='custom')
    add1.delay(x, y)
    add2.delay(x, y)
    return "done"
