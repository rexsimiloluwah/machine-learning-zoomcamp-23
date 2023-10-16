.PHONY: build-docker-image run-docker-container 

DOCKER_IMAGE_NAME=ml-zoomcamp-module-5-docker-web-example 

build-docker-image:
	docker build -t ${DOCKER_IMAGE_NAME} .

run-docker-container:
	docker run -p 9696:9696 -it ${DOCKER_IMAGE_NAME}