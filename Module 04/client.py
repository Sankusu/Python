#!/usr/bin/python3 

# This is client.py file

import socket


# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


# get local machine name
host = socket.gethostname()


# port number same as server
port = 9999


# connection to hostname on the port.
clientsocket.connect((host, port))


# Receive no more than 1024 bytes
msg = clientsocket.recv(1024)

print(msg.decode('ascii'))

clientsocket.close()