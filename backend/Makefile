SHELL := /bin/bash
PWD := $(shell pwd)

default: build

all:

docker-image:
	docker build -f ./Dockerfile -t "secure-api-rest-backend:latest" .
.PHONY: docker-image

run-server: docker-image
	docker run -p 5000:5000 -it --rm --name secure-api-rest-backend secure-api-rest-backend:latest
.PHONY: run-server