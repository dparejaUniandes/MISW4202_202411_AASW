from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime, timezone, timedelta


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

@app.route("/", methods=('POST',))
def hello_world():
    nuevo_registro = Monitor(numeroPrueba=request.json['numeroPrueba'],\
                            duracionDeteccion=request.json['duracionDeteccion'],\
                            fechaCreacion=datetime.now(timezone(timedelta(hours=-5), 'CT')),\
                            esFalla=request.json['esFalla'])
    db.session.add(nuevo_registro)
    db.session.commit()
    return monitor_schema.dump(nuevo_registro)

@app.route("/")
def getMonitores():
    monitor_logs = []
    with open('monitor_log.csv', 'w') as file:
        file.write('{},{},{},{}\n'.format("prueba", "duración_detección", "fecha", "es_falla"))
        for monitor in Monitor.query.all():
            file.write('{},{},{},{}\n'.format(monitor.numeroPrueba, monitor.duracionDeteccion, monitor.fechaCreacion, monitor.esFalla))
            monitor_logs.append(monitor_schema.dump(monitor))
    return monitor_logs

db.init_app(app)
db.create_all()

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)