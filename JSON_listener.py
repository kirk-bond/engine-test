import json
import socket
import sys
from threading import *

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = socket.gethostname()
port = int(sys.argv[1])
s.bind((host, port))
s.listen(20)


class ThreadedClient(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            clientsocket, addr = s.accept()
            print("Connection:")
            try:
                json.loads(test.decode())
            except Exception as e:
                clientsocket.sendall("Invalid JSON format: %s") % e
            else:    
                clientsocket.sendall("Received valid flag input: %s") % test


while True:
    clientsocket, address = s.accept()
    ThreadedClient(clientsocket, address)
