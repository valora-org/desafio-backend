FROM python:3.8-alpine3.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code 

RUN python3 -m pip install --upgrade pip

COPY req.txt req.txt 

RUN pip install -r req.txt 

COPY . /code


CMD ["gunicorn","desafio_config.asgi:application","--bind","0.0.0.0:8080","-w","4","-k","uvicorn.workers.UvicornH11Worker"]