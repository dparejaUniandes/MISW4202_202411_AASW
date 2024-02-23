from flask import Flask, request
from redis import Redis
from rq import Queue
from sender import monitor_heartbeat

app = Flask(__name__)

q = Queue(connection=Redis(host='redis', port=6379, db=0))

@app.route("/")
def hello_world():
    return "<p>Hello, World! from parametros de salud</p>"

@app.route("/", methods=('POST',))
def beat():
    q.enqueue(monitor_heartbeat, {
        'numeroPrueba': request.json['numeroPrueba'],
        'duracionDeteccion': request.json['duracionDeteccion'],
        'candado': request.json['candado']
    })
    return {
        "numeroPrueba": request.json['numeroPrueba'],
        "duracionDeteccion": request.json['duracionDeteccion']
    }

if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)