import logging
from flask import Flask, request, jsonify
import redis
import time
import threading
import random
from datetime import datetime

# Configura el registro de Flask para que no se escriba en el mismo archivo
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

# Configura el registro principal para las señales "alive"
logging.basicConfig(filename='heartbeat.log', level=logging.INFO)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
app = Flask(__name__)

# Ruta para ejecutar logíca de monitoreo de parametros de salud
@app.route("/")
def hello_world():
    return "<p>Dato de salud recibido</p>"

def enviar_señales_alive(duracion_experimento):
    inicio_experimento = time.time()
    while time.time() - inicio_experimento < duracion_experimento:
        if random.random() < 0.05:  # Probabilidad de falla de x%
            logging.info("Simulando falla en el envío de señales de monitoreo")
            time.sleep(0.5)  # Simula una falla de x segundos
            continue  # Salta al siguiente ciclo sin enviar señales
        # Obtiene la fecha y hora actual con 3 decimales de precisión
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        # Guarda la señal de "alive" en el log con la fecha y hora actual
        logging.info(f'Señal de alive enviada a la cola en {fecha_hora_actual}')
        # Se publica mensaje en cola de Redis
        redis_client.publish('heartbeat', fecha_hora_actual)
        time.sleep(0.1)
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    logging.info(f'Se finaliza experimento {fecha_hora_actual}')

def start_heartbeat_thread(duracion_experimento):
    heartbeat_thread = threading.Thread(target=enviar_señales_alive, args=(duracion_experimento,))
    heartbeat_thread.start()


# Ruta para iniciar el experimento
@app.route("/iniciar_experimento", methods=["POST"])
def iniciar_experimento():
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    logging.info(f'Se inicia experimento {fecha_hora_actual}')
    duracion_experimento = request.json.get("duracion_experimento", 100)  # Duración predeterminada de 100 segundos
    start_heartbeat_thread(duracion_experimento)
    return jsonify({"mensaje": "Experimento iniciado correctamente"})

if __name__ == "__main__":
    start_heartbeat_thread()
    app.run(host="0.0.0.0", port=5000, debug=True)
