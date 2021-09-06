FROM python:3.8.5-buster

RUN apt update && apt install -y apt-transport-https ca-certificates sqlite3

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
