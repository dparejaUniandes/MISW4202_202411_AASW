# modules
from modelos import MonitorSchema, Monitor
from app import db
import time

monitor_schema = MonitorSchema()

def save_log(numeroPrueba, duracionDeteccion, fechaCreacion):
    log = Monitor(numeroPrueba=numeroPrueba,
                            duracionDeteccion=duracionDeteccion,
                            fechaCreacion=fechaCreacion
                    )
    db.session.add(log)
    db.session.commit()

def watch_dog():
    ultimo_log = Monitor.query.order_by(Monitor.id.desc()).first()

    if not ultimo_log:
        print("No hay logs")
        return
    
    while True:
        fecha_actual = time.time()
        diferencia = fecha_actual - ultimo_log.fechaCreacion.timestamp()
        print("Diferencia: ", diferencia)
        time.sleep(0.5)


    # while True:
    #     fin = time.time()
    #     diferencia = fin - inicio
    #     if diferencia != 0 and diferencia % 0.5 == 0:
    #         print("Hubo una falla", (fin - inicio))
    #         inicio = time.time()
    #         nuevo_registro = Monitor(numeroPrueba=1,\
    #                         duracionDeteccion=1,\
    #                         fechaCreacion=datetime.now(timezone(timedelta(hours=-5), 'CT')),\
    #                         esFalla=True)
    #         with app.app_context():
    #             db.session.add(nuevo_registro)
    #             db.session.commit()

