# client.py  
import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()

port = 12345

# connection to hostname on the port.
clientsocket.connect((host, port))

# Receive no more than 1024 bytes
tm = clientsocket.recv(1024)

clientsocket.close()

print("The time got from the server is", tm.decode('ascii'))