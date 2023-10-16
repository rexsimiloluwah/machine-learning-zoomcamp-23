.PHONY: build-docker-image run-docker-container 

DOCKER_IMAGE_NAME=ml-zoomcamp-module-5-assignment

build-docker-image:
	docker build -t ${DOCKER_IMAGE_NAME} .

run-docker-container:
	docker run -p 9697:9697 -it ${DOCKER_IMAGE_NAME}