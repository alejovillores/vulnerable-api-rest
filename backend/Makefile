SHELL := /bin/bash
PWD := $(shell pwd)

default: build

all:

docker-image:
	docker build -f ./Dockerfile -t "insecure-api-rest-backend:latest" .
.PHONY: docker-image

run-server: docker-image
	docker run -p 5000:5000 -it --rm --name insecure-api-rest-backend insecure-api-rest-backend:latest
.PHONY: run-server