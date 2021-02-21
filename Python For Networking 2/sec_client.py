import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8081))
print("* * * Connected to server * * *")

data = client_socket.recv(1024)
message = data.decode()
print(message)

while True:
    data = client_socket.recv(1024)
    message = data.decode()
    print(message)
