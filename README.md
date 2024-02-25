# MISW4202_202411_AASW

Repositorio para el 3er ciclo de MISO para la materia Arquitecturas ágiles de software

## Instrucciones de reproducción experimento: 

1. Clonar el repositorio en local.  
2. Ejecutar `docker compose up --build --force-recreate`
3. Desde postman hacer solicitud get a url: `http://localhost/parametros-salud`, debe responder `<p>Dato de salud recibido</p>` (En este paso se deben configurar las 30 peticiones por segundo recurrentes para simular carga de trabajo al microservicio).
![1](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/5012b30b-a09c-4b30-b3d6-6dacdd8b8a30)
4. Desde postman hacer solicitud get a url: `http://localhost/monitor`, debe responder `<p>Hello, world from monitor, trabajando de forma correcta</p>`. En este paso se realiza la suscripción del monitor a la cola de mensajes.
![2](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/1615058f-3ba6-444e-bece-3957ab8243c0)
5. Desde postman enviar el comando post a url: `http://localhost/parametros-salud/iniciar_experimento`, incluir Body raw JSON indicando duración del experimento en segundos y porcentaje de falla. Debe responder `{ mensaje: Experimento iniciado correctamente }`
![3](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/4fccf743-ab8d-4ff4-be33-f09755cd41c8)
6. En vscode revisar los archivos `hearbeat.log` y `hearbeat_received.log` donde se encuentran almacenados los datos enviados por el componente monitoreado y los datos recibidos por el monitor hearbeat a través de la cola de mensaje.
![4](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/ee34bd74-023c-4e3a-99f9-5bf0c2c27b44) ![5](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/4e94dd3c-e566-489f-a15a-ff94498ba199)

