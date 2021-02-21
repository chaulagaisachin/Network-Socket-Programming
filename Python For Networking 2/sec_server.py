import socket

# Creating a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()
print("* * * Waiting for Connection * * *")
connection_socket, address = server_socket.accept()
print("Connected to client: ", address)

# # Sending message
# message = "Hello, this is server !!!"
# data = message.encode()
# connection_socket.send(data)

while True:
    message = input("Enter the Message: == ")
    data = message.encode()
    connection_socket.send(data)
