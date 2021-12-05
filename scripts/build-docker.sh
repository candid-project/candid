#!/bin/bash
readonly service="$1"

docker build -t "gcr.io/scenic-cedar-324901/$service" "." -f "./docker/$service/Dockerfile"
docker push "gcr.io/scenic-cedar-324901/$service"
