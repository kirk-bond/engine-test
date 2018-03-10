import json
import socket
import sys

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = socket.gethostname()
port = int(sys.argv[1])
s.bind((host,port))
s.listen(20)

while True:
    clientSocket, addr = s.accept()
    try:
        json.loads(addr)
    except Exception as e:
        s.send("Invalid JSON format: %s") %e
    clientSocket.close()
