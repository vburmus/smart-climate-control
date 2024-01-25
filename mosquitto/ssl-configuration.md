# How to make it work? 
## Certificate generation

```
openssl genrsa -des3 -out ca.key 2048
openssl req -new -x509 -days 1833 -key ca.key -out ca.crt
```
## Server certificate generation
```
openssl genrsa -out server.key 2048
openssl req -new -out server.csr -key server.key
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360
```
## Client certificate generation
```
openssl genrsa -out client.key 2048
openssl req -new -out client.csr -key client.key
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 360
```
## Give permissions for user and for mosquitto service to files
```
sudo chown user:user(mosquitto:mosquitto) keys_directory/*.* 
```