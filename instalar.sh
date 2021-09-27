#!/bin/sh

docker-compose build &&
docker-compose up -d &&
sleep 60
docker-compose down