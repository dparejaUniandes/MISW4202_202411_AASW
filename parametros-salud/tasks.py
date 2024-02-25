from celery import Celery
import redis


# Crea una instancia de Redis
redis_client = redis.StrictRedis(host='broker', port=6379, db=0)
# Configura la conexión con Redis
celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',  # URL de conexión a Redis
    backend='redis://redis:6379/0'  # URL de conexión a Redis para el resultado de las tareas
)

# Define una tarea Celery para enviar señales de vida
@celery.task
def enviar_señales_alive():
    redis_client.publish('heartbeat', 'alive')

# Define una tarea Celery para recibir señales de vida
@celery.task
def recibir_señales_alive():
    # Suscribe al cliente de Redis a la clave 'heartbeat'
    pubsub = redis_client.pubsub()
    pubsub.subscribe('heartbeat')
    # Escucha continuamente las señales de heartbeat
    for mensaje in pubsub.listen():
        # Verifica si el mensaje es una señal de heartbeat
        if mensaje['type'] == 'message':
            # Procesa el mensaje recibido (puede guardar el registro en un archivo de registro)
            print(f"Señal de alive recibida: {mensaje['data'].decode()}")
