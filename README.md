# Machine Learning App Deployment on Amazon EKS

This project demonstrates how to deploy a machine learning app to an Amazon EKS cluster. The app is a simple gender classification model that is built using Streamlit and containerized using Docker. The Docker image is hosted on Docker Hub and deployed to an Amazon EKS cluster. The project also incorporates MLOps practices such as version control, continuous integration and deployment (CI/CD), and infrastructure as code (IaC).

## Implementation Steps

1. **Model Creation**: Created and saved the machine learning model as a pickle file in Colab.
2. **App Development**: Developed a Python file (app.py) in a project folder to load the model and create the application using Streamlit.
3. **Dependency Management**: Generated a requirements.txt file using pip freeze to capture the necessary dependencies.
4. **Containerization**: Constructed a Dockerfile to containerize the application, built the Docker image, and pushed it to a Docker Hub repository.
5. **AWS Configuration**: Configured AWS CLI with access and secret keys for seamless interaction with AWS services.
6. **Kubernetes Setup**: Installed kubectl and eksctl to manage the AWS EKS cluster.
7. **EKS Cluster Creation**: Used eksctl to create an Amazon EKS cluster.
8. **App Deployment**: Deployed the containerized Streamlit application on the EKS cluster using the Docker image from Docker Hub. The deployment was defined in a .yaml file (streamlit-app-deployment.yaml).
9. **Kubernetes Configuration**: The .yaml file contains two sections: 'Deployment' and 'Service'. The 'Deployment' section specifies the container name, Docker image, number of replicas, resource allocation, and port configuration. The 'Service' section acts as a load balancer for the application, exposing the application pods as network services accessible via an IP address. The pods utilize the TCP protocol and operate on port 80 of the EKS cluster.
10. **Application Launch**: Deployed the application using the command 'kubectl apply -f streamlit-app-deployment.yaml'.
11. **Version Control**: Implemented version control using Git and DVC for data and code versioning.
12. **Continuous Integration and Deployment (CI/CD)**: Set up AWS CodePipeline with AWS CodeBuild for continuous integration and deployment. The pipeline is configured using a buildspec.yml file.
13. **Infrastructure as Code (IaC)**: Used Terraform to manage the AWS resources as code.

## Repository Files

- `Dockerfile`: This file contains the instructions to build the Docker image for the Streamlit application.
- `app.py`: This is the main Python file that loads the machine learning model and creates the Streamlit application.
- `buildspec.yml`: This file is used by AWS CodeBuild to build and push the Docker image. It also includes commands to update the Docker image in the Kubernetes deployment and apply the changes to the EKS cluster.
- `dataset/`: This directory contains the dataset used to train the machine learning model.
- `main.tf`: This is the Terraform configuration file that defines the AWS resources.
- `models/`: This directory contains the trained machine learning model saved as a pickle file.
- `requirements.txt`: This file lists the Python dependencies that are required to run the application.
- `streamlit-app-deployment.yaml`: This is the Kubernetes configuration file that defines the deployment and service for the Streamlit application on the EKS cluster.
