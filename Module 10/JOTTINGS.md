# Kubernetes & Tensorflow Serving 

## 10.1 Overview 
- We will use Tensorflow serving for serving the trained Tensorflow model for cloth classification
- Tensorflow serving is optimized for inference
- Tensorflow serving uses `gRPC`

## 10.2 Tensorflow Serving
- Saving the model using the `saved model` format
- Serving the model using TF Serving packaged in a Docker container 
- Performing inference on the served model

## 10.3 Creating the Gateway service using Flask 
- Create a gateway service using Flask for interacting with the TF Serving server
- Test the endpoint for obtaining predictions 

## 10.4 Docker compose
- Create a stand-alone image for the TF Serving instance and the Flask gateway service
- Create a Docker-compose file for defining the multi-container application to ensure communication between the Flask gateway service and the TF serving instance

## 10.5 Introduction to Kubernetes 
- Kubernetes is a container orchestration platform for deploying, managing, and scaling containerized applications.
- Kubernetes ensures scalability, high availability etc.
- Components of the Kubernetes architecture include the Kubernetes cluster, control plane, Node, pods, service, ingress controller, container runtime, etcd etc.
    1. **Kubernetes cluster**: A K8s cluster is a group of individual machines, known as "nodes", that work together to run containerized applications and manage them.
    2. **Control Plane**: This is the **Master Node** of the K8s cluster. It is the "brain" of the K8s cluster, and it control and coordinates all the activities in the K8s cluster. It typically includes the following components:
       - **API Server**: Entry point for interacting with the cluster, and handling requests from users
       - **etcd**: Distributed key-value store for storing the cluster configuration and state
       - **Scheduler**: For resource management
       - **Controller manager**: Monitors the cluster's state and makes decisions to ensure that the desired state is maintained.
    3. **Node**: Nodes refer to the worker machines which run on the K8s cluster. These worker machines could be physical or virtual servers which hold the pods/containers.
    4. **Pods**: A Pod is a deployable unit which contains one or more containers with shared network and storage for creating application instances.
    5. **Service**: A service is an entrypoint to the pods, it enables access to the pods internally/externally and routes requests to the pods.
    6. **Ingress controller**: An ingress controller is used to control the amount of traffic from the outside inside the pod.
- A **Kubernetes Deployment** is used to deploy, manage, and scale a group of identical pods running instances of the application. 
  - Deployments are described using the container images and number of replicas
  - It ensures that a specified number of pods (replicas) are running at any time using the deployment controller. 
  - It also spins up a new pod to replace any pod which is down or unhealthy. 
  - It also uses rolling updates to ensure a seamless update when the deployment configuration is changed, with minimal disruption
  - The application can be automatically scaled by increasing the number of replicas 

- `kubectl` is a tool for interacting with any Kubernetes cluster.

## 10.6 Deploying a simple service to Kubernetes
- Start the Kubernetes cluster (i.e. using minikube)
```bash
minikube start

## Check the cluster status
minikube status 
```

- Install `kubectl` for AWS. This is helpful if you will be running the cluster on AWS EKS.

- Configure `kubectl` to use the specific Kubernetes cluster 

- Example commands
  - Get the services in the K8s cluster
  ```bash
  kubectl get service
  ```

  - Get the pods in the K8s cluster
  ```bash
  kubectl get pod
  ```

  - Get the deployments in the K8s cluster
  ```bash
  kubectl get deployment
  ```

  - To provide detailed information about various Kubernetes resources such as pods, nodes, services, deployments, configmaps, secrets for debug/troubleshoot issues in the K8s cluster:
  ```bash
  kubectl describe <RESOURCE_TYPE> <RESOURCE_NAME>

  # Examples
  ## Get information about a pod
  kubectl describe pod <POD_NAME>

  ## Get information about a service
  kubectl describe service <SERVICE_NAME>

  ## Get information about a deployment
  kubectl describe deployment <DEPLOYMENT_NAME>

  ## Get information about a node
  kubectl describe node <NODE_NAME>

  ## Get information about a configmap or a secret
  kubectl describe configmap <CONFIGMAP_NAME>
  kubectl describe secret <SECRET_NAME>
  ```

  - To create, update, or delete resources in the Kubernetes cluster. We use the `apply` command:
  ```bash
  # Create or Update
  kubectl apply -f /path/to/<resource>.yml

  # Delete
  kubectl delete -f /path/to/<resource>.yml
  ```

- We can use port-forwarding to create a secure tunnel between our local computer and a pod running on a Kubernetes cluster. This gives us access to the application running on the pod. To create this port-forwarding using `kubectl`:
```bash
# The `REMOTE_PORT` is the port on the pod
kubectl port-forward <POD_NAME> <LOCAL_PORT>:<REMOTE_PORT>
```

- `ClusterIP` is an internal service while `LoadBalancer` is an external service. `ClusterIP` is the default service type.

- We can also port-forward to the service 
```bash
kubectl port-forward <SERVICE_NAME> <LOCAL_PORT>:<REMOTE_PORT>
```

## 10.7 Deploying the TF-SERVING instance and the Gateway service to Kubernetes

- To use local docker images in Minikube, we need to load the image into the Minikube Docker daemon

```bash
minikube image load <image_name>
```

- Create the deployment configuration for the TF serving model
```bash
kubectl apply -f kube-config/model-deployment.yml
```

- Use port forwarding to enable access to the TF serving model pod
- Create the TF Serving service and port-forward it
```bash
kubectl apply -f kube-config/model-service

# port-forwarding
kubectl port-forward service/tf-serving-clothing-model-service 8500:8500
```

- Enter the bash of another pod to test connection to the TF serving host on the `tf-serving-clothing-model-service` service
```bash
kubectl exec -it <POD_NAME> -- bash

# Test the service access
apt install curl telnet 
telnet tf-serving-clothing-model-service.default.svc.cluster.local 8500
```

- Create the deployment for the gateway and expose the pod using port-forwarding 
```bash
kubectl apply -f kube-config/gateway-deployment.yml

# port-forwarding 
kubectl port-forward <POD_NAME> 9696:9696
```

- Create the service for the gateway and expose it using port-forwarding 
```bash
kubectl apply -f kube-config/gateway-service.yml

# port-forwarding 
kubectl port-forward service/gateway-clothing-model-service 8090:80
```

## 10.8 Deploying to EKS
- This will mostly involve creating an EKS cluster on AWS, publishing the docker images to ECR, and configuring `kubectl` to work with the EKS cluster.

- We can create this from the AWS EKS web console or us the `eksctl` CLI.

- Create the EKS cluster from a YAML configuration file

- Publish the docker images to a public container registry i.e. DockerHub or AWS ECR 

- `kubectl` should be configured to interact with the `eksctl` cluster

- Create the resources (deployment, services) on the Kubernetes cluster for the model
```bash
kubectl apply -f kube-config/model-deployment.yml
kubectl apply -f kube-config/model-service.yml
```

- Create the resources (deployment, services) on the Kubernetes cluster for the gateway
```bash
kubectl apply -f kube-config/gateway-deployment.yml
kubectl apply -f kube-config/gateway-service.yml
```
