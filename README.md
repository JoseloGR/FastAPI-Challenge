# Point of Sale Test

Prueba desarrollada con el framework de FastAPI, usando Python como lenguaje de programación.


## Instalación y ejecución del backend

Se debe tener instalado docker-compose antes de correr el siguiente comando.

Como primer paso será crear el archivo `.env` usando el `.env.sample`, donde prácticamente sólo se debe cambiar el password y el nombre de la base de datos, los demás valores deben permanecer con el mismo valor para el correcto funcionamiento.

El siguiente comando creará todo el ambiente para correr el backend y el servicio de base de datos (PostgreSQL)

```bash
docker-compose up -d --build
```

### Servidor de backend

Se levantará el servidor en el puerto 8000

Para poder ver la documentación de los endpoints deberás acceder a `http://localhost:8000/docs`
