# Microservicio de Adquisición de Datos
Este microservicio se encarga de la adquisición de datos desde cámaras IP y su almacenamiento en AWS S3.

## Estructura del Proyecto

bifrost-data-acquisition/
main.py: Punto de entrada de tu aplicación FastAPI.
models.py: Modelos Pydantic para validación y serialización de datos.
routers/
cameras.py: Rutas relacionadas con la interacción con las cámaras IP.
storage.py: Rutas relacionadas con el almacenamiento de imágenes en AWS S3.
utils/
rtsp_utils.py: Funciones auxiliares para capturar imágenes desde RTSP.
storage_utils.py: Funciones auxiliares para interactuar con AWS S3.
tests/: Pruebas para el microservicio.
requirements.txt: Lista de dependencias del proyecto.
README.md: Documentación y detalles del proyecto.

Esta estructura ayuda a mantener el proyecto organizado y modular, facilitando el desarrollo y mantenimiento del microservicio.

