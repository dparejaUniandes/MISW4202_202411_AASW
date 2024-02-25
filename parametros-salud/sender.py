from celery import Celery

celery_app = Celery('tasks', broker='redis://redis/0')

@celery_app.task(name="heartbeat")
def monitor_heartbeat(data):
    pass