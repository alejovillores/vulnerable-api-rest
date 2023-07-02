SHELL := /bin/bash
PWD := $(shell pwd)

default: build

all:

docker-image:
	docker build -f ./Dockerfile -t "secure-api-rest-frontend:latest" .
.PHONY: docker-image

run-client: docker-image
	docker run -p 4200:4200 -it --rm --name secure-api-rest-frontend secure-api-rest-frontend:latest
.PHONY: run-client