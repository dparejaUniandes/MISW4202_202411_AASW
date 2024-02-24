from datetime import datetime, timezone, timedelta
from app import *
import threading
import time
import requests
import json

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

def monitor_heartbeat(data_info):
    print("monitor_heartbeat *** ")
    data_json={"numeroPrueba": data_info['numeroPrueba'],"duracionDeteccion":data_info['duracionDeteccion'],"candado": data_info['candado']}
    headers = {'content-type': 'application/json'}
    content = requests.post('http://172.21.0.5:5000', headers=headers,
                            json=data_json)
    if content.status_code != 200:
        print ("Error:", content.status_code)
    else:
        monitor_log = content.json()
        print(json.dumps(monitor_log))
    print("Mensaje recibido en monitor_heartbeat")
    
    # db.session.add(nuevo_registro)
    # db.session.commit()
    # print(monitor_schema.dump(nuevo_registro))
    # run_thread(data['candado'], app)
    # print([monitor_schema.dump(monitor) for monitor in Monitor.query.all()])
