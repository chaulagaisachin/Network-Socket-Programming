# Importing socket module
import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding physical address
server_socket.bind(("127.0.0.1", 8081))

# Listening state
server_socket.listen()

print("* * * * WAITING FOR CONNECTION * * * * ")

# Accept Incoming Connection
connection_socket,  address = server_socket.accept()

# Information
print(connection_socket)
print(address)

# Sending Message
while True:
    message = input("Enter any message == ")
    if message == "":
        connection_socket.close()
        server_socket.close()
        break
    data = message.encode()
    connection_socket.send(data)

