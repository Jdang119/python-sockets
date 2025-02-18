# project pseudocode
# Create a Socket
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

