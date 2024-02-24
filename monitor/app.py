from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime, timezone, timedelta
import time
import threading
from queue import Queue


db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/monitor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

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

monitor_schema = MonitorSchema()

db.init_app(app)
db.create_all()