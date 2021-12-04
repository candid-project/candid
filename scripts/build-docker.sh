#!/bin/bash
readonly service="$1"

docker build -t "gcr.io/scenic-cedar-324901/$service" "./src" -f "./docker/$service/Dockerfile"
docker push "gcr.io/scenic-cedar-324901/$service"
