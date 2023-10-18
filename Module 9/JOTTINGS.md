- AWS Lambda provides serverless compute services using event-triggered functions

### Converting the model to a tensorflow lite version
- We need to convert the Tensorflow model to TF-LITE to stay within the AWS Lambda limits, improve inference speed, reduce memory usage.

### Preparing a Docker Image for deployment on AWS Lambda 
- Search for desired base image on AWS ECR public image repository

- Create the Dockerfile and build the docker image

- Run the Docker container and test it

### Creating the Lambda Function

- We will publish the Docker image to AWS ECR 

- Create an AWS ECR repository
```bash
aws ecr create-repository --repository-name clothing-tflite-model
```
- Keep the repository URI -> 323725762285.dkr.ecr.us-east-1.amazonaws.com/clothing-tflite-model

- Authentication -> Logging in to the repository (Specify the correct account profile using the `--profile` argument if necessary)
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

- Tag the image

- Push the image to the AWS ECR repository

- 

- 



### Exposing the Lambda Function using AWS API Gateway

- Go to the AWS API Gateway console
- Create new REST API (`REST API` > `BUILD`)
- Create a resource for the specific endpoint i.e. `predict`
- Create a `POST` request method under the resource
- Add the Lambda function to be invoked by the `POST` request method
