# msa-k8s-mp4tomp3-converter
Building a service that mimics the behaviour of online services to convert mp4/video files to mp3/audio files. Files are downloaded when user in authenticated.

The application follows a modern microservice architechture orchestrated by **kubernetes**.

## Architecture
The following diagram highlights the architecture of the application as well as its lifecycle generating an mp3 file 

![MSA architecture for converting file](https://user-images.githubusercontent.com/50111205/209007685-9bd6eb52-10d1-4831-a554-2ca0a59f6acc.png)

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
