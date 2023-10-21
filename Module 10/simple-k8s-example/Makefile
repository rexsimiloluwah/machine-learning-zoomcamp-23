.PHONY: build-docker-image run-docker-container

IMAGE_NAME=simple_k8s_example

build-docker-image:
	docker build -t ${IMAGE_NAME} .

run-docker-container:
	docker run -it --rm -p 9698:9698 ${IMAGE_NAME}