from flask import Flask
from flask import request
from modelos import db, Usuario

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db.init_app(app)

@app.route("/status")
def hello_world():
    return "<p>Login working!</p>"

#Endpoint para iniciazlizar base de datos
@app.route("/init_db")
def hinit_db():
    from init_db import init_db
    init_db()
    return {"msg": "Database initialized"}

@app.route("/", methods=["POST"])
def login():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username:
        return {"msg": "Missing username parameter"}, 400
    if not password:
        return {"msg": "Missing password parameter"}, 400

    user = db.session.query(Usuario).filter_by(
        usuario=username, contrasena=password).first()
    if not user:
        return {"msg": "Bad username or password"}, 401

    return {"msg": "login correcto, solicitar token al servicio Autorizador."}


if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)