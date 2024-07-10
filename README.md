# Pizza ordering app using Django

This project is based on an assignment for a coding test

## Requirements

this project is settled for two main parts:

1. Order Placement Form: A form that allows users to place orders for pizza. This form
should include:
a. A dropdown menu for selecting the type of pizza (e.g., Margherita, Pepperoni,
Vegetarian, etc.).
b. A text area for comments or special instructions.
2. Orders Table: A page that displays all placed orders in a tabular format. Each row
should display the type of pizza ordered and any comments associated with the order.


## Installation

1. Open terminal using Ctrl+T. Run the following command <br>
`git clone https://github.com/k4mus/mypizza.git`

2. Create and active virtual environment using  <br>
` virtualenv venv` <br>
`source venv/bin/activate` <br>
4. Now you need to install python packages to run the app <br>
`pip install -r requirements.txt`
5. Create superuser <br>
 `python manage.py createsuper`
6. Run Django app <br>
`python manage.py runserver`

## Tech Stack

- **Django**  Django is a Python-based free and open-source web framework,
 which follows the model-view-template architectural pattern. It is maintained by the Django Software
 Foundation, an independent organization established as a 501 non-profit.[Django Project](https://www.djangoproject.com/) <br>
It is used in this project, to handle all routes, rendering pages and managing databases.

- **Minikube** [minikube](https://minikube.sigs.k8s.io/docs/start/) is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.
All you need is Docker container or a Virtual Machine environment, and Kubernetes is a single command away: `minikube start`

## Deployment Requirements:
1. Containerization: Containerize the web application using Docker. Provide a Dockerfile in your repository.
2. Kubernetes Deployment: Deploy your application to Kubernetes. Should include the necessary Deployments, Services, and any other resources needed to make the application accessible.
* Ensure the application is scalable and can handle multiple instances.

## Deployment local with minikube:
to run this locally, make sure that you have mikube installed and running, then execute the following commands:
start the minube cluster:
`minikube start`
execute the deployment and service using the public registry </br>
- `cd .k8s`
- `kubectl apply -f deployment.yaml`
- `kubectl apply -f service.yaml`
- `minikube service mypizza-service`
