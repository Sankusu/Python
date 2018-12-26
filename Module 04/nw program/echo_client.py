# echo_client.py

import socket

host = socket.gethostname()
port = 9999					# The same port as used by the server

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

print("Client created...")

sent_msg = 'Hello World'
clientsocket.send(sent_msg.encode("ascii"))
print('Message Sent:', sent_msg)

recv_msg = clientsocket.recv(1024)

print('Message Received:', recv_msg.decode("ascii"))

clientsocket.close()