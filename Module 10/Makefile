.PHONY: run-tf-serving-clothing-model 

TF_SERVING_MODEL_IMAGE_NAME=mlzoomcamp-10-model:xception-v4 
FLASK_GATEWAY_IMAGE_NAME=mlzoomcamp-10-gateway 

run-tf-serving-clothing-model:
	PWD="$(shell pwd)"

	docker run -it --rm \
		-p 8500:8500 \
		-v "${PWD}/clothing_model:/models/clothing_model/1" \
		-e MODEL_NAME="clothing_model" \
		tensorflow/serving:2.7.0

build-tf-serving-model-image:
	docker build \
		-t ${TF_SERVING_MODEL_IMAGE_NAME} \
		-f tfserving-model.dockerfile .

run-tf-serving-model-container:
	docker run -it --rm \
		-p 8500:8500 \
		${TF_SERVING_MODEL_IMAGE_NAME}

build-flask-gateway-image:
	docker build \
		-t ${FLASK_GATEWAY_IMAGE_NAME} \
		-f gateway.dockerfile .

run-flask-gateway-container:
	docker run -it --rm \
		-p 9696:9696 \
		${FLASK_GATEWAY_IMAGE_NAME}

create-eks-cluster:
	eksctl create cluster -f kube-config/eks-cluster-config.yml

delete-eks-cluster:
	eksctl delete cluster --name <cluster_name>