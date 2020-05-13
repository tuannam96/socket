import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Server is running...")
while True:
    clientsocket, address = s.accept()
    print("connection from {} has been established.".format(address))
    clientsocket.send(bytes("hey, there !!!", "utf-8"))
    clientsocket.close()
