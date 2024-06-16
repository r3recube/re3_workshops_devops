# Workshop DevOps

## Obiettivi del Workshop

Questo workshop è progettato per fornire una comprensione pratica dell'utilizzo di Terraform per gestire l'infrastruttura su AWS, implementare microservizi su un cluster EKS e creare pipeline CI/CD automatizzate. Al termine di questo workshop, i partecipanti saranno in grado di:

1. Creare e configurare un cluster EKS utilizzando Terraform.
2. Implementare microservizi Docker su un cluster EKS.
3. Configurare e gestire una pipeline CI/CD per il deployment continuo dei microservizi.
4. Implementare strumenti di osservabilità per monitorare e tracciare le applicazioni.

## Struttura del Workshop

Il workshop è suddiviso in quattro laboratori principali:

### Lab-1: Creare un Cluster EKS usando Terraform

#### Task-0: Setup

Install yum-config-manager to manage your repositories.

`sudo yum install -y yum-utils`

Use yum-config-manager to add the official HashiCorp Linux repository.

`sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo`

Install Terraform from the new repository

`sudo yum -y install terraform`

Clone the repository

`git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/<username>`

Initialize Terraform

`terraform init`

#### Task-1: Complete the Manifest file

on `terraform.tfvars` set the variable with the following:
- owner = your name, lowercase without space (ex. paololatella)
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
module "eks_managed_node_group" {
  source = "terraform-aws-modules/eks/aws//modules/eks-managed-node-group"
  ...
}
```
Reference: https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest/submodules/eks-managed-node-group

#### Task-3: Add an Application Load Balancer**

Complete the ALB Configuration on Terraform Manifest

```
module "alb" {
  source = "terraform-aws-modules/alb/aws"
  ...
}
```
Reference: https://registry.terraform.io/modules/terraform-aws-modules/alb/aws/latest


#### Task-4: Create EKS Cluster and related resources**

Validate the Terraform template

`terraform validate`

Create an execution plan

`terrafom plan`

Apply the changes

`terraform apply`

#### Task-5: Look on EKS Cluster resources**

Install kubectl: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

Update kubectl config

`aws eks update-kubeconfig --region region-code --name <your-name>-my-eks-cluster`

See PODS and Namespaces


### Lab-2: Implementare i tuoi Microservizi

**Task-1: Creare la tua prima immagine Docker**

Retrieve an authentication token and authenticate your Docker client to your registry.

`aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 983441761380.dkr.ecr.eu-west-1.amazonaws.com`

### Bikes Microservices
Locate Bikes Microservice

Build your Docker image using the following command.

`docker build -t bikes:latest .`

Tag your image so you can push the image to this repository:

`docker tag bikes:latest 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-bikes-ecr-repository:latest`

Run the following command to push this image to your newly created AWS repository:

`docker push 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-bikes-ecr-repository:latest` 

### Cars Microservices
Locate Cars Microservice

Build your Docker image using the following command.

`docker build -t cars:latest .`

Tag your image so you can push the image to this repository:

`docker tag cars:latest 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-cars-ecr-repository:latest`

Run the following command to push this image to your newly created AWS repository:

`docker push 983441761380.dkr.ecr.eu-west-1.amazonaws.com/<your-name>-cars-ecr-repository:latest` 

**Task-2: Distribuire il tuo primo POD sul Cluster EKS**

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

**Task-1: Creare un progetto CodeBuild**
- Configurare un progetto AWS CodeBuild per automatizzare la build dell'immagine Docker.

**Task-2: Creare una CodePipeline**
- Configurare una pipeline AWS CodePipeline per automatizzare il processo di build e deploy.

**Task-3: Distribuire Microservizi con Deployment Blue/Green**
- Implementare una strategia di deploy Blue/Green per minimizzare i tempi di inattività.

### Lab-4: Implementare l'Osservabilità

**Task-1: Aggiungere Logging e Metriche**
- Configurare il logging e le metriche per monitorare le prestazioni e il funzionamento delle applicazioni.

**Task-2: Aggiungere il Tracing**
- Implementare il tracing distribuito per tracciare le richieste attraverso i microservizi.

## Prerequisiti

Prima di iniziare, controlla che le seguenti risorse cloud sono disponibili nel tuo account AWS:
- Ambiente Cloud9
- Registro Docker
- VPC
- Repository Codice e Infrastruttura 

- 

