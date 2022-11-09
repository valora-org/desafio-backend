#base image
FROM python:3.9

RUN mkdir /app
WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PORT=8888

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py create_admin

EXPOSE 8888

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT