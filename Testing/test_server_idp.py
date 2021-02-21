import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("127.0.0.1", 2222))

while True:
    data, client_address = udp_server.recvfrom(1024)
    print(data)