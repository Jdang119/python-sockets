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

#sending a message to the server
#converting string to raw bytes before sending using utf-8
message = "Hello, server!"
client_socket.send(message.encode("utf-8"))

#receiving a response from the server
#decoding raw bytes of data from server into readable format
#setting it to a response variable
response = client_socket.recv(1024).decode("utf-8")
print(f"Server response: {response}")


#closing connection
client_socket.close()