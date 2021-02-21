import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 8081))

print("Connected")

while True:
    data = client_socket.recv(1024)
    message = data.decode()
    if message == "":
        client_socket.close()
        break
    print(message)
