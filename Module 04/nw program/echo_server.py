# echo_server.py

import socket

host = socket.gethostname()			# Symbolic name meaning all available interfaces
port = 9999							# Arbitrary non-privileged port

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# bind to the port
serversocket.bind((host, port))

print("Server created...")
print("host:", host)
print("port:", port)


# queue up to 1 requests
serversocket.listen(1)


while True:
	# establish a connection
	clientsocket, addr = serversocket.accept()
	print('Connected by', addr)
	
	# Receive no more than 1024 bytes
	data = clientsocket.recv(1024)

	clientsocket.send(data)

	clientsocket.close()