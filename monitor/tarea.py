from celery import Celery
from celery.signals import task_postrun
# modules
from services import save_log

celery_app = Celery('tasks', broker='redis://redis/0')

@celery_app.task(name="heartbeat")
def registrar_beat(data):
    print("from heartbeat", data)
    numeroPrueba = data.get("numeroPrueba", None)
    duracionDeteccion = data.get("duracionDeteccion", None)
    fechaCreacion = data.get("fechaCreacion", None)
    save_log(numeroPrueba, duracionDeteccion, fechaCreacion)

@task_postrun.connect()
def close_session(*args, **kwargs):
    pass