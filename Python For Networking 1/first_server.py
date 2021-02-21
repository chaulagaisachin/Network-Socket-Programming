import socket

# Creating a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the physical address in the socket object.
server_socket.bind(("127.0.0.1", 8081))

# Socket object listening to any connection
server_socket.listen()

print("* * * Waiting for Connection * * *")
connection_socket, address = server_socket.accept()

print("Connected to a client")
print("Info about connection == ", connection_socket)
print("Connected to client ==  ", address)

message = input("Enter your message == ")
data = message.encode()
connection_socket.send(data)

server_socket.close()
connection_socket.close()

