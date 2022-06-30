from celery import shared_task
from celery import Celery

@shared_task
def test():
    for i in range(10):
        print(i)
    return "done"