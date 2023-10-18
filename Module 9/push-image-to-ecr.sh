ACCOUNT_ID=323725762285
REGION=us-east-1
PREFIX=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

LOCAL_TAG=clothing-model
REMOTE_TAG=clothing-tflite-model
REMOTE_REPOSITORY_URI=${PREFIX}/${REMOTE_TAG}:latest

docker tag ${LOCAL_TAG}:latest ${REMOTE_REPOSITORY_URI}
docker push ${REMOTE_REPOSITORY_URI}