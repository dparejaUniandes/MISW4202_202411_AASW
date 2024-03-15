from flask import Flask
from flask import request
from modelo import db, Usuario, InfoDemografica, UsuarioSchema, db
from init_db import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app_context = app.app_context()
app_context.push()

db.init_app(app)

db.create_all()
init_db()

usuario_schema = UsuarioSchema()

@app.route("/", methods=["PUT"])
def modify_demographic_information():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    username = request.json.get("username", None)
    token = request.json.get("token", None)
    edad = request.json.get("edad", None)
    peso = request.json.get("peso", None)
    estatura = request.json.get("estatura", None)
    genero = request.json.get("genero", None)
    pais = request.json.get("pais", None)
    return "<p>Hello, World! from usuario</p>"

""" Lo que se envia en la peticion desde el cliente
{
                "username": "",
                "token": "",
                "edad": 1,
                "genero": "",
                "pais": "
            }
"""

@app.route("/<username>")
def obtener_informacion_demografica(username):
        #return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()] trae todos
        return usuario_schema.dump(Usuario.query.filter_by(usuario=username).first())

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)