FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY . /src/
RUN pip install pipenv
RUN pipenv install