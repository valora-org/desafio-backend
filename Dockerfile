FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

# Install postgres client
RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --ignore-pipfile --deploy

COPY . /code/
