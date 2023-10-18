.PHONY: build-docker-image

build-docker-image:
	docker build -t clothing-model .

run-docker-container:
	docker run -it --rm -p 8080:8080 clothing-model:latest