# MISW4202_202411_AASW

Rama para Experimento de Validación de seguridad

## Semana 8
### Experimento 2

## Instrucciones de reproducción experimento: 

1. Clonar el repositorio en local.
2. Moverse a la rama `validacion_seguridad`
3. Ejecutar `docker compose up --build --force-recreate` para cargar los contenedores, en algunos computadores puede ser necesario poner un guión entre docker y compose, es decir `docker-compose up --build --force-recreate`, con este comando quedará disponible el **nginx** que servirá como Api Gateway, el microservicio de **Login** que permite la autenticación de usuarios, el microservicio **Autorizador** que genera tokens de seguridad, los valida y los elimina y el microservicio **Usuario** que se encarga de modificar la información demográfica para un usuario autorizado, si no está autorizado el usuario, manda una solicitud al microservicio Login para que revoque la sesión.
4. Desde postman hacer solicitud post a url: `localhost/cliente/iniciar-experimento`, incluir Body raw JSON indicando el atributo repeticiones, que permite simular la cantidad de peticiones que se van a realizar y el porcentaje_falla que indica el porcentaje que queremos que falle la autorización, es decir, es el porcentaje que queremos que un usuario no esté autorizado al realizar la operación de modificar información demográfica para que se pueda revocar la sesión.
<img width="1284" alt="image" src="https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142551793/754e218f-1b34-46c4-a145-a7b30548b5d6">
5. Cuando finalice el experimento se debe obtener la siguiente respuesta:<br>
<img width="406" alt="image" src="https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142551793/1531e68d-29a8-46c2-9e90-56db4434b62b"> <br>
6. En vscode o el editor de preferencia, se puede apreciar que en la carpeta del microservicio cliente se genera un archivo peticiones.log, donde se puede evidenciar todas las peticiones que se realizaron, las cuales pueden mostrar si hubieron un error o si el proceso estuvo bien, también se identifica en caso de haber error con el número 0 y en caso de no haber error con el número 1.

**Se simulan 100 peticiones con un porcentaje de falla de 20**
<img width="1086" alt="image" src="https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142551793/9fc874d0-510b-4faa-b3a0-ab2bac93466b">
7. En vscode o el editor de preferencia, se puede apreciar que en la carpeta del microservicio Autorizador se genera un archivo tiempo1.log, donde se puede evidenciar todas las las detecciones que se presentaron con respecto a tokens de seguridad inválidos, estos se identifican con **no_autorizado**, y también se muestran todos los logs que dan cuenta de la eliminación del token para revocar la sesión del usuario, estos se identifican con **token_removido**, esto se hace con el fin de guardar los tiempos de detección y de reacción y evaluar si el experimento pudo revocar la sesión de un usuario en menos de 1 segundo cuando se detectó la no autorización de modificación de información demográfica.
<br>
<img width="803" alt="image" src="https://github.com/dparejaUniandes/MISW4202_202411_AASW/assets/142551793/b504496f-98d3-4cf7-84e4-8c986893e336">

