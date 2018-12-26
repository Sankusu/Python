# server.py 
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()
port = 12345

# bind to the port
serversocket.bind((host, port))

# queue up to 1 requests
serversocket.listen(1)

while True:
	# establish a connection
	clientsocket, addr = serversocket.accept()

	print("Got a connection from %s" % str(addr))
	
	currentTime = "test"
	clientsocket.send(currentTime.encode('ascii'))
	clientsocket.close()