FROM python:3.8

RUN python -m pip install -U pip

COPY ./requirements.txt /requirements.txt
COPY ./requirements-test.txt /requirements-test.txt

RUN	pip install -r /requirements.txt && \
    pip install -r /requirements-test.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user