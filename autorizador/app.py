from flask import Flask, request
from db import connect_to_db, db
from models import User
from utils import generate_token, NOT_FOUND_MSG, NOT_AUTHORIZED_MSG, OK_MSG, SESION_REMOVED_MSG
import logging
from datetime import datetime

# Configura el registro de Flask para que no se escriba en el mismo archivo
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)

# Configura el registro principal para las señales "alive"
logging.basicConfig(filename='tiempo1.log', level=logging.INFO)

app = Flask(__name__)
connect_to_db(app)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World! from autorizador</p>"

@app.route("/validar-token", methods=["POST"])
def validar_token():
    username = request.json.get("username", None)
    token = request.json.get("token", None)

    if(username is None or token is None):
        return { "msg": NOT_FOUND_MSG, "estado": False }, 400

    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        return { "msg": NOT_AUTHORIZED_MSG, "estado": False }, 401

    if user.token != token:
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d:%H:%M:%S.%f')[:-3]
        logging.info(f"no_autorizado: {fecha_hora_actual}")
        return {"msg": NOT_AUTHORIZED_MSG, "estado": False }, 401
    
    return { "msg": OK_MSG, "estado": True }, 200

@app.route("/generar-token", methods=["POST"])
def generate_user_token():
    
    username = request.json.get("username", None)
    if username is None:
        return {"msg": NOT_FOUND_MSG}, 400

    user = db.session.query(User).filter_by(username=username).first()
    token = generate_token()

    if not user:
        user_to_save = User(username=username, token=token)
        db.session.add(user_to_save)
        db.session.commit()
        return { "msg": OK_MSG, "token": token }, 200
    
    user.token = token
    db.session.commit()

    return { "msg": OK_MSG, "token": token }, 200

@app.route("/remover-token", methods=["POST"])
def remove_user_token():

    username = request.json.get("username", None)

    if username is None:
        return { "msg": NOT_FOUND_MSG, "estado": False }, 400

    user = db.session.query(User).filter_by(username=username).first()

    if not user:
        return { "msg": NOT_FOUND_MSG, "estado": False }, 400
    
    db.session.delete(user)
    db.session.commit()
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d:%H:%M:%S.%f')[:-3]
    logging.info(f"token_removido: {fecha_hora_actual}")
    return { "msg": SESION_REMOVED_MSG, "estado": True }, 200
    

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)