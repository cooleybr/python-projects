# This project demonstrates a flask server using ssl certificates 

## Components:
 - create-certs.sh - may need to chmod +x to run, will create certs, copy, and remove top level directory
 - Server - Makes endpoints available on https://localhost:5000
 - Client - Makes endpoints available on http://localhost:6000
 - docker-compose.yml - defines the docker network and containers

## Introduction:
The application starts a server on 5000 accessible only to services with the appropriate certificates (client). The create-certs.sh script creates the requisite cert, ca, and key files then copies these to each of the services in a subdirectory "certs"

When the containers load, the client home page is accessible without certificates, but the server root is not.

A call to the http://localhost:6000/test endpoint will make an authenticated SSL request to the server and return the response text.

## Usage: 

 - Clone the repo and cd into the directory
 - ./create-certs.sh - creates a temporary directory, generates server and client certs, and copies these to their respective services
 - docker-compose up - should download the python:3 container image, copy the appropriate files, and start the containers

 When running:
 - docker ps should show 2 containers (healthy)
 - make a get request to http://localhost:5000 - should provide empty reply
 - make a get request to http://localhost:6000 - should return client
 - make a get request to http://localhost:6000/test - should return "got server"

 - docker-compose down


