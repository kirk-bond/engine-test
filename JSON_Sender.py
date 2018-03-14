import json
import socket
import sys

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

jsonString = {"test" : "data"}
sendString = json.dumps(jsonString)
s.connect((host, port))
s.send(sendString.encode())
# s.send(jsonString.encode())
result = s.recv(1024)
print(result)
s.close()
