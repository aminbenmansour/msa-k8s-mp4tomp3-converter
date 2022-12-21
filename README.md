# msa-k8s-mp4tomp3-converter
Building a service that mimics the behaviour of online services to convert mp4/video files to mp3/audio files. Files are downloaded when user in authenticated.

The application follows a modern microservice architechture orchestrated by **kubernetes**.

## Usage
make sure you have the following requirements installed
* python
* docker
* kubernetes
* kubectl
* minikube
* k9s (optional): make it easier to navigate, observe and manage your deployed applications in the wild.

steps for running the application
1. whithin each folder containing a `requirements.txt` file run these bash commands
 ```
 python3 -m venv env && source ./env/bin/activate
 ```
 
 ```
 pip3 install -r requirements.txt
 ```
 
 2. inside each `manifests` folder run
 ```
 kubectl apply -f ./
 ```
