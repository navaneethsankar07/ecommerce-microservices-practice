# E-Commerce Microservices

A simple **E-Commerce Microservices** project built for learning and practicing Microservices Architecture using **Django**, **Docker**, and **Kubernetes**.

> **Note:** This project is created for learning purposes to understand how microservices are built, containerized, and orchestrated. It is **API-only** and is **not intended for production use**.

---

## 🚀 Features

* User Service
* Product Service
* Order Service
* REST-based inter-service communication
* Separate PostgreSQL database for each service
* Dockerized services
* Kubernetes deployment
* Health check endpoints

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* Kubernetes

---

## 📁 Project Structure

```text
ecommerce-microservices/
│
├── user-service/
├── product-service/
├── order-service/
│
└── k8s/
    ├── user/
    ├── product/
    ├── order/
    └── postgres/
```

---

## 🏗️ Architecture

```text
                 +----------------+
                 | Order Service  |
                 +----------------+
                    /          \
                   /            \
                  ▼              ▼
        +---------------+   +----------------+
        | User Service  |   | Product Service|
        +---------------+   +----------------+
               │                    │
               ▼                    ▼
        PostgreSQL DB        PostgreSQL DB

               │
               ▼
        Order PostgreSQL DB
```

Each service owns its own database and communicates with other services using REST APIs.

---

## 📌 Services

### User Service

* Manage users
* User CRUD APIs
* Health endpoint

### Product Service

* Manage products
* Product CRUD APIs
* Stock validation
* Health endpoint

### Order Service

* Create orders
* Validates user and product through REST APIs
* Health endpoint

---

## 🐳 Docker

Each service includes its own:

* Dockerfile
* requirements.txt

Docker is used to containerize every service independently.

---

## ☸️ Kubernetes

The project includes Kubernetes manifests for:

* Deployments
* Services
* PostgreSQL databases
* Environment variables

The application can be deployed on a Kubernetes cluster such as Minikube.

---

## 📡 API Only

This project contains **backend APIs only**.

You can test the APIs using:

* Postman
* curl
* Insomnia

---

## 📚 Learning Objectives

This project was built to practice:

* Microservices Architecture
* REST communication between services
* Docker image creation
* Docker networking
* PostgreSQL integration
* Kubernetes Deployments
* Kubernetes Services
* Environment variables
* Container orchestration
* Persistent storage

---

## 🔮 Future Improvements

* API Gateway
* JWT Authentication
* RabbitMQ / Kafka
* Redis Caching
* CI/CD Pipeline
* Monitoring & Logging
* Production deployment
* Frontend application

---

## 📄 License

This project is created for educational and learning purposes.
