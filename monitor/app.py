from flask import Flask
import redis
import logging
from datetime import datetime
import threading

#Configura el registro de Flask para que no se escriba en el mismo archivo
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

# Configura el registro principal para las señales "alive"
logging.basicConfig(filename='heartbeat_received.log', level=logging.INFO)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
app = Flask(__name__)

@app.route("/")
def hello_world():
    start_heartbeat_thread()
    return "<p>Hello, World! from monitor, trabajando de forma correcta</p>"

def recibir_heartbeat():
    # Suscribe al cliente de Redis a la clave 'heartbeat'
    pubsub = redis_client.pubsub()
    pubsub.subscribe('heartbeat')
    timestamp_anterior = None
    # Escucha continuamente las señales de heartbeat
    for mensaje in pubsub.listen():
        # Verifica si el mensaje es una señal de heartbeat
        if mensaje['type'] == 'message':
            timestamp_actual = datetime.now()
            if timestamp_anterior is not None:
                dif_time = (timestamp_actual - timestamp_anterior).total_seconds() * 1000
                if dif_time > 500:
                    logging.info("Falla detectada")
                else:
                    # Registra la fecha y hora de la recepción en el log
                    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    logging.info(f"Señal de alive recibida a la hora: {fecha_hora_actual}")
            timestamp_anterior = timestamp_actual

def start_heartbeat_thread():
    heartbeat_thread = threading.Thread(target=recibir_heartbeat)
    heartbeat_thread.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)