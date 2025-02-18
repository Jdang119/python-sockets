# Create Client Side Socket
# Connect to serverSide's IP and port
# Send a message to the server
# Wait for a response from the server
# print the servers response
# close the connection

import socket


#Creating Client Socket (same as serverSide)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting to serverSide Server
#assumed client has the known address and theoretical "hostname" of server address
server_address = ("127.0.0.1", 12345)
client_socket.connect(server_address)
print("Connected to the server")

