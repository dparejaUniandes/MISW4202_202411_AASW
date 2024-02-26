# MISW4202_202411_AASW

Repositorio para el 3er ciclo de MISO para la materia Arquitecturas ágiles de software

## Instrucciones de reproducción experimento: 

1. Clonar el repositorio en local.
2. Moverse a la rama `async`
3. Ejecutar `docker compose up --build --force-recreate` para cargar los contenedores, en algunos computadores puede ser necesario poner un guión entre docker y compose, es decir `docker-compose up --build --force-recreate`
4. Desde postman hacer solicitud get a url: `http://localhost/parametros-salud`, debe responder `<p>Dato de salud recibido</p>` Con este paso se verifica que el microservicio esta en ejecución.  
![1](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/5012b30b-a09c-4b30-b3d6-6dacdd8b8a30)  
5. Desde postman hacer solicitud get a url: `http://localhost/monitor`, debe responder `<p>Hello, world from monitor, trabajando de forma correcta</p>`. Con este paso se verifica que el microservicio esta en ejecución y se garantiza la suscripción del microservicio a la cola de mensajes. Se debe realizar la solicitud una sola vez para que exista un único suscriptor.   
![2](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/1615058f-3ba6-444e-bece-3957ab8243c0)
6. Desde postman configurar y correr un Runner para realizar solicitudes al microservicio de parametros de salud simulando una carga de trabajo normal de 30 solicitudes por segundo.
![7](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/b4877431-526b-480c-934e-08bc24545fb0)  
8. Desde postman enviar el comando post a url: `http://localhost/parametros-salud/iniciar_experimento`, incluir Body raw JSON indicando duración del experimento en segundos y porcentaje de falla (Es el porcentaje de mensajes que se envían con el fin de generar una falla) `{"duracion_experimento": 10,"porcentaje_falla": 8, "duracion_falla": 1}`. Debe responder `{ mensaje: Experimento iniciado correctamente }`
![6](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/adfac636-3e19-4c90-b084-a9d372b7f92c)  
9. En vscode revisar los archivos `hearbeat.log` y `hearbeat_received.log` donde se encuentran almacenados los datos enviados por el componente monitoreado y los datos recibidos por el monitor hearbeat a través de la cola de mensaje.
![4](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/ee34bd74-023c-4e3a-99f9-5bf0c2c27b44) ![5](https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142282285/4e94dd3c-e566-489f-a15a-ff94498ba199)

