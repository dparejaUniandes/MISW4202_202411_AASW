from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

def init_db(app):
    # db should be global    
    db = SQLAlchemy(app)



class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numeroPrueba = db.Column(db.Integer)
    duracionDeteccion = db.Column(db.Integer)
    fechaCreacion = db.Column(db.DateTime)
    esFalla = db.Column(db.Boolean)

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.numeroPrueba, self.duracionDeteccion, self.fechaCreacion)

class MonitorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Monitor
        load_instance = True