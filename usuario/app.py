from flask import Flask
from flask import request
from modelo import db, Usuario, InfoDemografica, UsuarioSchema, db, InfoSchema
from init_db import init_db

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
    usuario = Usuario.query.filter_by(usuario=username).first()
    token = request.json.get("token", None)
    usuario.info_demografica.edad = request.json.get("edad", usuario.info_demografica.edad)
    usuario.info_demografica.peso = request.json.get("peso", usuario.info_demografica.peso)
    usuario.info_demografica.estatura = request.json.get("estatura", usuario.info_demografica.estatura)
    usuario.info_demografica.genero = request.json.get("genero", usuario.info_demografica.genero)
    usuario.info_demografica.idioma = request.json.get("idioma", usuario.info_demografica.idioma)
    usuario.info_demografica.pais = request.json.get("pais", usuario.info_demografica.pais)
    db.session.commit()

    infoDemografica = InfoDemografica.query.filter_by(id=usuario.info_demografica.id).first()
    return info_schema.dump(infoDemografica)

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