import socket
import sys
from random import random
import pandas

# https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
buffer_size = 4096
filename = "id.xml"
HOST = '127.0.0.1'
PORT = 10000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    print("Connecting to:", HOST, PORT)
    sock.connect((HOST,PORT))
    print("Connected!")
    sock.send(f"{filename}".encode())
    with open(filename,"rb") as data:
        reader = data.read(buffer_size)
        sock.sendall(reader)
    data = sock.recv(buffer_size).decode()
    file_to_client = data
    print("data received from server:", file_to_client)
    with open(file_to_client,"wb") as f2:
        read = sock.recv(buffer_size)
        f2.write(read)
sock.close()

#filesize = os.path.getsize

