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


# Streaming problem.
def send_text(sending_socket, text):
    text = text + "\n"
    data = text.encode()
    sending_socket.send(data)


# New send code
message = "Hello"
send_text(connection_socket, message)
