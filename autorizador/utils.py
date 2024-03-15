import base64
from datetime import datetime

def generate_token():
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    now_bytes = now_str.encode('utf-8')
    now_base64 = base64.b64encode(now_bytes)
    
    return now_base64.decode('utf-8')

NOT_FOUND_MSG = "Valide los datos de consulta"
NOT_AUTHORIZED_MSG = "No autorizado"
OK_MSG = "los datos son correctos"