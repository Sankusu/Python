#!/usr/bin/python3

# This is server.py file

import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 1 requests
serversocket.listen(1)



while True:
	# establish a connection
	clientsocket, addr = serversocket.accept()
	print("Got a connection from", addr)

	msg = 'Thank you for connecting'

	clientsocket.send(msg.encode('ascii'))

	clientsocket.close()