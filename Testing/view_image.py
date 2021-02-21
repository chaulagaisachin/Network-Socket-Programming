from fl_networking_tools import ImageViewer
import socket
import pickle

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("127.0.0.1", 2222))

lost_pixels = 0
last_pixel_updated = (-1, -1)

# Define a function called get_pixel_data, that will wait for data to be received on the UDP socket
def get_pixel_data():
    lost_pixels = 0
    last_pixel_updated = (-1, -1)
    while True:
        data, client_address = udp_server.recvfrom(1024)
        message = pickle.loads(data)
        pos = message[0]
        rgba = message[1]
        viewer1.put_pixel(pos, rgba)
        if (pos[0] - last_pixel_updated[0] > 1) or (pos[1] - last_pixel_updated[1] > 1):
            lost_pixels += 1
            viewer1.text = lost_pixels
        last_pixel_updated = pos


viewer1 = ImageViewer()
viewer1.text = lost_pixels
viewer1.start(get_pixel_data)

