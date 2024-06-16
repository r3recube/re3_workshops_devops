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

**Task-0: Setup**

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

**Task-1: Add Managed Node Group to EKS**

Complete the Node Group Configuration on Terraform Manifest

```
module "eks_managed_node_group" {
  source = "terraform-aws-modules/eks/aws//modules/eks-managed-node-group"
  ...
}
```
Reference: https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest/submodules/eks-managed-node-group

**Task-2: Add an Application Load Balancer**

Complete the ALB Configuration on Terraform Manifest

```
module "alb" {
  source = "terraform-aws-modules/alb/aws"
  ...
}
```
Reference: https://registry.terraform.io/modules/terraform-aws-modules/alb/aws/latest


**Task-3: Create EKS Cluster and related resources**

Validate the Terraform template

`terraform validate`

Create an execution plan

`terrafom plan`

Apply the changes

`terraform apply`

### Lab-2: Implementare i tuoi Microservizi

**Task-1: Creare la tua prima immagine Docker**
- Creare un'immagine Docker per un microservizio e caricarla su DockerHub.

**Task-2: Distribuire il tuo primo POD sul Cluster EKS**
- Distribuire un pod utilizzando l'immagine Docker nel cluster EKS.

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

