from modelos import db, Usuario, InfoDemografica

def init_db(check_existing=True):
    if check_existing:
        existing_users = Usuario.query.all()
        if existing_users:
            print("La base de datos ya tiene usuarios. No es necesario inicializarla nuevamente.")
            return

    if not check_existing:
        print("Eliminando la base de datos existente...")
        db.drop_all()
        db.create_all()

    usuarios = [
        {"usuario": "usuario1", "contrasena": "password1", "edad": 25, "genero": "M", "idioma": "ES", "pais": "ES"},
        {"usuario": "usuario2", "contrasena": "password2", "edad": 30, "genero": "F", "idioma": "EN", "pais": "US"},
    ]

    for u in usuarios:
        usuario = Usuario(usuario=u["usuario"], contrasena=u["contrasena"])
        db.session.add(usuario)

        info_demografica = InfoDemografica(
            edad=u["edad"],
            genero=u["genero"],
            idioma=u["idioma"],
            pais=u["pais"],
            usuario=usuario  
        )
        db.session.add(info_demografica)

    db.session.commit()
    print("Base de datos inicializada y usuarios agregados con éxito.")

if __name__ == "__main__":
    init_db()
