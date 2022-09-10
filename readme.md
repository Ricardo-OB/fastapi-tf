# FastAPI y Tensorflow

[<img src="https://geekflare.com/wp-content/uploads/2019/07/fast-api-logo.png" width="20%">](https://fastapi.tiangolo.com/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<img src="https://cdn-images-1.medium.com/fit/t/1600/480/0*B8VDCnh8qBnwUuM4" width="30%">](https://www.tensorflow.org/hub)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<img src="https://miro.medium.com/max/888/0*eQv7rTU0f_0jMOeg.jpeg" width="20%">](https://locust.io/)

API creada con FastAPI y Tensorflow, la cual predice un objeto segun los datos (imagenes) de [ImageNet](https://www.image-net.org/). La arquitectura utilizada es [MobileNet V2](https://arxiv.org/abs/1801.04381), se empleo la arquitectura pre-entrenada y subida en Tensorflow Hub.

## Pasos

1. Clona el repositorio

2. Crea y activa el entorno virtual

3. Instala los requerimientos: `pip install -r requirements.txt`

4. Ejecuta la API en tu equipo (localhost): `python .\src\main.py`

5. Dirigete a http://localhost:8000/docs (documentación automatica de FastAPI)

6. Busca una imagen y copia el URL. Luego pega el URL en el endpoint `/predict/tf` (petición de tipo POST). 

    Ejemplo:

        "url_image": "https://raw.githubusercontent.com/Ricardo-OB/fastapi-tf/master/src/images/golden.jpg"

    Debe aparecerte esta respuesta (predicción del objeto y su probabilidad asociada):

        "predicted_label": "golden retriever",
        "probability": 0.9514861106872559

## Contenerización (Docker :whale:)

Si deseas desplegar la API dentro de un contenedor con ayuda de Docker sigue los siguientes pasos:

1. Ejecuta `docker-compose up --build` para construir y subir la imagen

2. Sigue los paso 5 y 6 descritos anteriormente

Nota: Si detienes el contenedor puedes volver a iniciarlo con el comando `docker start fastapicontainer`


