import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8081))
# print("* * * Connected to server * * *")

# data = client_socket.recv(8)
# message = data.decode()
# print(message)


def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open:
        # read any data from the socket
        data = receiving_socket.recv(8)

        # if no data is returned the socket must be closed
        if not data:
            socket_open = False

        # add the data to the buffer
        buffer = buffer + data.decode()

        # is there a terminator in the buffer
        terminator_pos = buffer.find("\n")
        print("first", terminator_pos)
        # if the value is greater than -1, a \n must exist
        while terminator_pos > -1:
            # get the message from the buffer
            message = buffer[:terminator_pos]
            print("buffer:term", message)
            # remove the message from the buffer
            buffer = buffer[terminator_pos + 1:]
            # yield the message (see below)
            yield message
            print("yield", message)
            print(terminator_pos)
            # is there another terminator in the buffer
            terminator_pos = buffer.find("\n")


# New Code
for message in get_text(client_socket):
    print(message)
