#!/bin/bash

mkdir ./certs

# Create CA
openssl req -passout pass:password -new -x509 -days 3650 -extensions v3_ca -keyout certs/ca_private.pem -out certs/ca.pem -subj '/CN=CA/OU=flask_certs/O=cooleybr/L=Utica/ST=NY/C=US'

# Create Key and Certificate Signing Requests

# Client 
openssl req -newkey rsa:4096 -nodes -out certs/client.csr -keyout certs/client.key -subj '/CN=client/OU=flask_certs/O=cooleybr/L=Utica/ST=NY/C=US'
openssl req -newkey rsa:4096 -nodes -out certs/server.csr -keyout certs/server.key -subj '/CN=server/OU=flask_certs/O=cooleybr/L=Utica/ST=NY/C=US'

# Sign the Certificate Signing Requests with the CA

# Client
openssl x509 -passin pass:password -sha256 -req -days 365 -in certs/client.csr -CA certs/ca.pem -CAkey certs/ca_private.pem -CAcreateserial -out certs/client-signed.crt
openssl x509 -passin pass:password -sha256 -req -days 365 -in certs/server.csr -CA certs/ca.pem -CAkey certs/ca_private.pem -CAcreateserial -out certs/server-signed.crt

# Create Server PEM
cat certs/client-signed.crt certs/client.key > certs/client.pem
cat certs/server-signed.crt certs/server.key > certs/server.pem

# Copy cert and ca files to services and database
mkdir ./client/certs/ # Make Directory to hold web-service certs
mkdir ./server/certs/ # Make directory to hold model-server certs
cp -t ./client/certs/ certs/client* certs/ca.pem
cp -t ./server/certs/ certs/server* certs/ca.pem
rm -rf certs