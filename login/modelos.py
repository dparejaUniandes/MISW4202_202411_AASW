from sqlalchemy import UniqueConstraint
from flask_sqlalchemy import SQLAlchemy
#from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Usuario(db.Model):
    __table_args__ = (UniqueConstraint('usuario', name='unique_username'),)
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    info_demografica = db.relationship('InfoDemografica', backref='usuario', uselist=False)

class InfoDemografica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    edad = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(1), nullable=False)
    idioma = db.Column(db.String(2), nullable=False)
    pais = db.Column(db.String(2), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)