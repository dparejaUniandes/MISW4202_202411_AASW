from celery import Celery
from celery.signals import task_postrun

celery_app = Celery('tasks', broker='redis://redis/0')

@celery_app.task(name="heartbeat")
def registrar_beat(data):
    print("from heartbeat", data)
    
@task_postrun.connect()
def close_session(*args, **kwargs):
    print("close session")