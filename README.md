# Workshop DevOps

## Obiettivi del Workshop

Questo workshop è progettato per fornire una comprensione pratica dell'utilizzo di Terraform per gestire l'infrastruttura su AWS, implementare microservizi su un cluster EKS e creare pipeline CI/CD automatizzate. Al termine di questo workshop, i partecipanti saranno in grado di:

1. Creare e configurare un cluster EKS utilizzando Terraform.
2. Implementare microservizi Docker su un cluster EKS.
3. Configurare e gestire una pipeline CI/CD per il deployment continuo dei microservizi.
4. Implementare strumenti di osservabilità per monitorare e tracciare le applicazioni.

## Struttura del Workshop

Il workshop è suddiviso in quattro laboratori principali:

### Prerequirements: Setup Your Environment

#### Task-1: Configure the AWS CLI

Disable AWS Managed Temporary Credentials on Cloud 9

Execute `aws configure` and put AK and SK related to you Cloudformation stack



### Lab - 1: Create your EKS Cluster with Terraform

#### Task-0: Install Terraform

Install yum-config-manager to manage your repositories.

`sudo yum install -y yum-utils`

Use yum-config-manager to add the official HashiCorp Linux repository.

`sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo`

Install Terraform from the new repository

`sudo yum -y install terraform`

Verify Terraform installation

`terraform -help`

#### Task-1: Initialize Terraform
Clone the repository

`git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/<username>`

Initialize Terraform

`terraform init`

on `terraform.tfvars` set the variable with the following:
- owner = *your name, lowercase without space (ex. paololatella)*
- aws_region = "eu-west-1"

Validate the Terraform template

`terraform validate`

Create an execution plan

`terrafom plan`

Apply the changes

`terraform apply`

#### Task-2: Add Managed Node Group to EKS

Complete the Node Group Configuration on Terraform Manifest

on file `main.tf`

```
resource "aws_eks_node_group" "eks_node_group" {
  cluster_name    = aws_eks_cluster.eks_cluster.name
  ...
}
```
Reference: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_node_group

Create an execution plan

`terrafom plan`

Apply the changes

`terraform apply`

### Lab - 2: Play with your EKS Cluster

#### Task-1: Install and Configure the kubectl

The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

Download kubectl

`curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl`

Setting permission and env

`chmod +x ./kubectl`
`mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH`
`echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc`

Verify installation

`kubectl version --client`

Update kubectl config

`aws eks update-kubeconfig --region region-code --name <your-name>-my-eks-cluster`

#### Task-2: Install and Configure the eksctl

eksctl is a simple CLI tool for creating and managing clusters on EKS - Amazon's managed Kubernetes service for EC2.

Setting Architecture

```
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH
```

Download the eksctl cli

`curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"`

Install the eksctl cli

```
tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz
sudo mv /tmp/eksctl /usr/local/bin
```

#### Task-3: Add an Application Load Balancer

##### Step 1: Create IAM Role using eksctl

Replace <your-name> with the name of your IAM account, <account-id> with your account ID, and then run the command.

```
eksctl create iamserviceaccount \
  --cluster=<yourname>-my-eks-cluster \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

Now you can proceed to install Load Balancer with HELM

##### Step 2: Install AWS Load Balancer Controller

Add the eks-charts Helm chart repository. AWS maintains this repository on GitHub.

`helm repo add eks https://aws.github.io/eks-charts`

Update your local repo to make sure that you have the most recent charts.

`helm repo update eks`

Install the AWS Load Balancer Controller.

Replace <your-name> with the name of your IAM account, <account-id> with your account ID, and then run the command.

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=<your-name>-my-eks-cluster \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller 
```

Verify that the controller is installed.

`kubectl get deployment -n kube-system aws-load-balancer-controller`

#### Task-4: Create EKS Cluster and related resources

Validate the Terraform template

`terraform validate`

Create an execution plan

`terrafom plan`

Apply the changes

`terraform apply`

Verify the created resources

#### Task-5: Look on EKS Cluster resources



See PODS and Namespaces


### Lab-2: Implementare i tuoi Microservizi

#### Task-1: Creare la tua prima immagine Docker

Retrieve an authentication token and authenticate your Docker client to your registry.

`aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 983441761380.dkr.ecr.eu-west-1.amazonaws.com`

Now you can start to create the microservices

##### Bikes Microservices
Locate Bikes Microservice

Build your Docker image using the following command.

`docker build -t bikes:latest .`

Tag your image so you can push the image to this repository:

`docker tag bikes:latest 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-bikes-ecr-repository:latest`

Run the following command to push this image to your newly created AWS repository:

`docker push 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-bikes-ecr-repository:latest` 

Your microservice is Up & Running

##### Cars Microservices
Locate Cars Microservice

Build your Docker image using the following command.

`docker build -t cars:latest .`

Tag your image so you can push the image to this repository:

`docker tag cars:latest 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-cars-ecr-repository:latest`

Run the following command to push this image to your newly created AWS repository:

`docker push 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-cars-ecr-repository:latest` 

Your microservice is Up & Running

#### Task-2: Distribuire il tuo primo POD sul Cluster EKS

Locate the bikes-deployment.yaml and update with the correct image url

```
containers:
  image: <image-url>
```

Deploy the bikes microservice

`kubectl apply -f bikes-deployment.yaml`

Locate the cars-deployment.yaml and update with the correct image url

```
containers:
  image: <image-url>
```

Deploy the cars microservice

`kubectl apply -f cars-deployment.yaml`


### Lab-3: Implementare una Pipeline CI/CD

#### Task-1: Creare un progetto CodeBuild
- Configurare un progetto AWS CodeBuild per automatizzare la build dell'immagine Docker.

#### Task-2: Creare una CodePipeline
- Configurare una pipeline AWS CodePipeline per automatizzare il processo di build e deploy.

#### Task-3: Distribuire Microservizi con Deployment Blue/Green
- Implementare una strategia di deploy Blue/Green per minimizzare i tempi di inattività.

### Lab-4: Implementare l'Osservabilità

#### Task-1: Aggiungere Logging e Metriche
- Configurare il logging e le metriche per monitorare le prestazioni e il funzionamento delle applicazioni.

#### Task-2: Aggiungere il Tracing
- Implementare il tracing distribuito per tracciare le richieste attraverso i microservizi.

## Prerequisiti

Prima di iniziare, controlla che le seguenti risorse cloud sono disponibili nel tuo account AWS:
- Ambiente Cloud9
- Registro Docker
- VPC
- Repository Codice e Infrastruttura 