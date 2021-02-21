from PIL import Image
import socket
import pickle

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
image1 = Image.open("photo1.jpeg")

width, height = image1.size

for y in range(height):
    for x in range(width):

        pos = (x, y)
        rgba = image1.getpixel(pos)
        print(pos, rgba)
        message = (pos, rgba)
        data = pickle.dumps(message)
        udp_client.sendto(data, ("127.0.0.1", 2222))

