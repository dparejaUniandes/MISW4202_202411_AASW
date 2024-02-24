from datetime import datetime, timezone, timedelta
from app import *
import threading
import time

def watch_dock(app):
    inicio = time.time()
    while True:
        fin = time.time()
        diferencia = fin - inicio
        if diferencia != 0 and diferencia % 0.5 == 0:
            print("Hubo una falla", (fin - inicio))
            inicio = time.time()
            nuevo_registro = Monitor(numeroPrueba=1,\
                            duracionDeteccion=1,\
                            fechaCreacion=datetime.now(timezone(timedelta(hours=-5), 'CT')),\
                            esFalla=True)
            with app.app_context():
                db.session.add(nuevo_registro)
                db.session.commit()

def run_thread(candado, app):
    print("Iniciar hilo")
    if candado == 0:
        thread = threading.Thread(target=watch_dock, args=(app,))
        thread.daemon = True
        thread.start()
        print("hilo iniciado")

def monitor_heartbeat(data):
    print("monitor_heartbeat *** ")
    nuevo_registro = Monitor(numeroPrueba=data['numeroPrueba'],\
                            duracionDeteccion=data['duracionDeteccion'],\
                            fechaCreacion=datetime.now(timezone(timedelta(hours=-5), 'CT')))
    db.session.add(nuevo_registro)
    db.session.commit()
    # print(monitor_schema.dump(nuevo_registro))
    run_thread(data['candado'], app)
    print([monitor_schema.dump(monitor) for monitor in Monitor.query.all()])
