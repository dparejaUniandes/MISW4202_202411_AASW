from celery import Celery
from celery.signals import task_postrun
# modules
from app import recibir_heartbeat

celery_app = Celery('tasks', broker='redis://redis/0')

@celery_app.task(name="heartbeat")
def registrar_beat(data):
    recibir_heartbeat()

@task_postrun.connect()
def close_session(*args, **kwargs):
    pass