from flask import Flask
from flask import request
from modelo import db, Usuario, InfoDemografica, UsuarioSchema, db, InfoSchema
from init_db import init_db
import requests
from utils import NOT_AUTHORIZED_MSG

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app_context = app.app_context()
app_context.push()

db.init_app(app)

db.create_all()
init_db()

usuario_schema = UsuarioSchema()
info_schema = InfoSchema()

@app.route("/", methods=["PUT"])
def modify_demographic_information():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    username = request.json.get("username", None)
    token = request.json.get("token", None)

    r = requests.post("http://autorizador:5000/validar-token", json={
                "username": username,
                "token": token
            })
    estado = r.json().get("estado", "")

    if estado:
        usuario = Usuario.query.filter_by(usuario=username).first()
        usuario.info_demografica.edad = request.json.get("edad", usuario.info_demografica.edad)
        usuario.info_demografica.peso = request.json.get("peso", usuario.info_demografica.peso)
        usuario.info_demografica.estatura = request.json.get("estatura", usuario.info_demografica.estatura)
        usuario.info_demografica.genero = request.json.get("genero", usuario.info_demografica.genero)
        usuario.info_demografica.idioma = request.json.get("idioma", usuario.info_demografica.idioma)
        usuario.info_demografica.pais = request.json.get("pais", usuario.info_demografica.pais)
        db.session.commit()

        infoDemografica = InfoDemografica.query.filter_by(id=usuario.info_demografica.id).first()
        return info_schema.dump(infoDemografica)
    else:
         return {"msg": NOT_AUTHORIZED_MSG}

""" Lo que se envia en la peticion desde el cliente
{
                "username": "",
                "token": "",
                "edad": 1,
                "genero": "",
                "pais": "
            }
"""

@app.route("/")
def obtener_informacion_demografica():
        #return usuario_schema.dump(Usuario.query.filter_by(usuario=username).first())
        return [info_schema.dump(info) for info in InfoDemografica.query.all()] 

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)