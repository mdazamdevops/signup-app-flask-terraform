# DevOps Internship Task 3 – Infrastructure as Code (IaC) with Terraform
### Elevate Labs: Empowering the Future of DevOps
This project is a testament to the high-quality, hands-on learning experience provided by Elevate Labs. Their internship program is dedicated to empowering the next generation of DevOps professionals by offering practical, real-world challenges that build foundational skills and a deep understanding of modern software development practices.

### Overview
The objective of this task is to provision a local Docker container using Terraform. This task provides hands-on experience with Infrastructure as Code (IaC), a fundamental practice in modern DevOps. By defining infrastructure in code, we can automate the provisioning process, making it repeatable, scalable, and version-controlled.

### Objective
Provision a local Docker container using Terraform.

Understand the core concepts of Infrastructure as Code.

Learn to use Terraform commands like init, plan, and apply.

### Tools & Technologies
Terraform – The open-source IaC tool used to define and provision infrastructure.

Docker – The containerization platform that serves as the target infrastructure for this task.

### Project Structure
```
.
├── .github/
│   └── workflows/
│       └── main.yml
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── frontend/
    ├── index.html
    ├── server.js
    ├── package.json
    └── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── main.tf
└── README.md
```

### Full Procedure: Step-by-Step Guide

### 1. Configure the Docker Provider
Terraform uses providers to interact with different platforms, such as AWS, Azure, or in this case, Docker. The first step is to configure the Docker provider in the main Terraform configuration file, typically named main.tf.

### 2. Write the Terraform Code
Next, you write the Terraform code to create the Docker container. This involves defining the docker_image and docker_container resources. The code specifies which image to use (e.g., nginx:latest), the container's name, and any port mappings.

### 3. Run Terraform Commands
a. Initialize the project:
```
terraform init
```
This command initializes the Terraform working directory and downloads the necessary Docker provider. It's the first command you run in a new or a cloned Terraform project.

b. Preview the changes:
```
terraform plan
```
This command creates an execution plan. It shows you exactly what Terraform will do—which resources will be created, changed, or destroyed—before any changes are applied to your infrastructure.

c. Apply the changes:
```
terraform apply
```
This command applies the changes required to reach the desired state defined in your main.tf file. It will create and run the Docker container as specified in your code. You will need to confirm the action by typing yes.

d. Destroy the infrastructure:
```
terraform destroy
```
After you are done with the infrastructure, you can use this command to stop and remove all resources created by Terraform. It's a clean way to tear down your environment.

4. Check the Terraform State
```
terraform state
```
This command provides information about the state of your infrastructure managed by Terraform. The state file (terraform.tfstate) is crucial as it maps the real-world resources to your configuration and keeps track of metadata.

## Learning Outcomes
By completing this task, you will:

* Understand the core principles and benefits of Infrastructure as Code.

* Gain practical experience with Terraform's workflow and command-line interface.

* Learn how to provision and manage a local Docker container using a declarative approach.

* Understand the role of Terraform's state file in managing infrastructure.

### Interview Questions to Practice
* What is IaC?
* How does Terraform work?
* What is the Terraform state file?
* Explain the difference between terraform apply and terraform plan.
* What are Terraform providers?
* What is resource dependency in Terraform?
* How do you handle secret variables in Terraform?
* Explain the benefits of using Terraform.

### Creator
Name: Mohd Azam Uddin
Role: DevOps Intern

* Contribution: Implemented a simple IaC project to provision a Docker container, providing a foundational understanding of Terraform.
