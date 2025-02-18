# project pseudocode
# Create a Server Socket
# Bind Socket to a specific port using .bind() (12345)
# Listen for incoming connections
# Accept Connection from a client
# Receive Message from client
# Send a Response back to the client
# Close Connection


import socket 
#socket is a built in library that provides functions and classes to create and manage network connections

#creating a socket object and assigning it to variable
#specifying address family with .AF_INET (IPV4)
#specifying socket type with .SOCK_STREAM (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#binding socket to an IP address and port
#setting IP address to localhost for testing
#arg for .bind is a tuple with IP and Port - otherwise TypeError occurs 
server_socket.bind(("127.0.0.1", 12345))


#listening for incoming connections
#.listen() set to allow only (1) connection at a time
server_socket.listen(1)
print ("Server is listening on port 12345..")

#accepting connection from a client (clientSide file)
#.accept() waits for incomming connection, returns new socket with new connection
client_socket, client_address = server_socket.accept()
print(f"Connection Established with {client_address}")

#receive message from client
#server is expecting to receieve and decode a message up to 1024 bytes 
#raw bytes from message are decoded into a readable string using utf-8 encoding
#setting received message to variable 
message = client_socket.recv(1024).decode("utf-8")
print (f"Received message: {message}")

#sending a response back to the client
#setting response message to response variable
#sending response data back to client encoded with UTF-8
response = "Message Received."
client_socket.send(response.encode("utf-8"))

#closing connections between both parties
client_socket.close()
server_socket.close()