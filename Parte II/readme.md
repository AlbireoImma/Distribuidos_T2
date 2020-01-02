# Tarea #2 Sistemas Distribuidos - 2019-II
## Parte II (chat rpc con [rabbitmq](https://https://www.rabbitmq.com/))

Para ejecutar el docker primero debemos construirlo:

> docker-compose build

Para levantar la arquitectura completa hacemos (nos solicitan 2 clientes al menos):

> docker-compose up --scale cliente=2

- Si los comandos no funcionan, el problema puede ser de permisos, usar sudo o su segun corresponda
- Se puede llamar el servicio cliente mas de una vez
- El directorio de los archivos del server esta en ./servidor
- El directorio de los archivos del cliente esta en ./cliente
- Para enviar mensajes desde el cliente se debe acceder a la consola de el, para esto al levantar con docker-compose up la arquitectura se imprimirá en la terminal el comando para abrirla, en donde debemos reemplazar el container correspondiente para usarlo (buscar container con docker container ls)

Comandos especiales del chat
- ?close - Cierra el chat y libera el nombre de usuario
- ?list - Muestra a todos los participantes del servidor
- ?chat - Muestra mensajes enviados por el usuario

Formato de los mensajes: *usuario mensaje* (ejemplo: user hola!)

**El nombre de usuario es unico y no tolera el uso de espacios**

Archivo servidor en ./Servidor.py

Archivo cliente en ./Cliente.py

Log autogenerado en ./servidor/log.txt cuenta con detalles de los mensajes
