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
            print("Connection")
            try:
                json.loads(addr.decode())
            except Exception as e:
                s.send("Invalid JSON format: %s") % e
            s.send("Received valid flag input: %s") % addr


while True:
    clientsocket, address = s.accept()
    ThreadedClient(clientsocket, address)
