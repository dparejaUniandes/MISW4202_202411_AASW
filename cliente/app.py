from flask import Flask, request, jsonify
from user import User
from services import login
import random
from services import update_user
import logging

# Configura el registro de Flask para que no se escriba en el mismo archivo
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

# Configura el registro principal para las señales "alive"
logging.basicConfig(filename='peticiones.log', level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! from cliente</p>"


def simular_modificacion(repeticiones, porcentaje_falla):
    i = 0
    
    while i < repeticiones:
        mensaje = "No hubo errores en la modificacion de datos"
        estado  = 1
        user = User("usuario1", "password1", "es", "token", "Colombia", "M", 31, 80, 170)
        token = login(user)

        if random.randint(1, 100) <= porcentaje_falla:
            mensaje = "Hubo un error en la modificacion de datos"
            estado  = 0
            token = ""
                           
        user.update_token(token)  
        update_user(user)
        logging.info(f"Repeticion {i}: {mensaje} : {estado}")
        print(f"Repeticion {i}: {mensaje} : {estado}")
        i += 1
    

@app.route("/iniciar-experimento", methods=["POST"])
def start_proof_of_concept():
    repeticiones = request.json.get("repeticiones", 100)  # Cantidad de repeticiones predeterminada de 100
    porcentaje_falla = request.json.get("porcentaje_falla", 20)  # Porcentaje de falla predeterminado de 20%
    simular_modificacion(repeticiones, porcentaje_falla)
    return jsonify({"mensaje": "Experimento finalizado correctamente"})



# @app.route("/iniciar-experimento")
# def start_proof_of_concept():
#     # create users
#     user1 = User("user1", "pwd1", "", "Colombia", "M", 31)
#     user2 = User("user2", "pwd2", "", "Panama", "F", 38)

#     # login
#     token1 = login(user1)
#     user1.update_token(token1)

#     token2 = login(user2)
#     user2.update_token(token2)

#     # update simulation

