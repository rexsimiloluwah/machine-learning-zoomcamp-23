## Deploying the model to AWS Elastic Beanstalk

- Install the AWS Elastic Beanstalk CLI (`awsebcli`)

- To install the Elastic Beanstalk CLI

```bash
pip install awsebcli 
```
- Initialize the Elastic Beanstalk project 

```bash 
eb init 
```

- Run the docker container locally using EB
```bash
eb local run --port 9696
```

- Create a new Elastic Beanstalk environment
```bash
eb create <environment_name> 
```

- Terminate the environment 
```bash
eb terminate <environment_name> 
```
