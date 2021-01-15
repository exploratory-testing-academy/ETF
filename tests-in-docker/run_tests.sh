#!/usr/bin/env bash

export PYTHONDONTWRITEBYTECODE=1

docker build --tag eprime-tests .

docker run --rm --net=host --security-opt seccomp:unconfined --shm-size "256M" -v $PWD:/app eprime-tests