import json
import socket
import sys

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

jsonString = {
  "actors": {
    "actor": [
      {
        "id": "1",
        "firstName": "Tom",
        "lastName": "Cruise"
      }
    ]
  }
}
sendString = json.dumps(jsonString)
print(sendString)
print(type(sendString))
s.connect((host, port))
s.send(sendString)
result = s.recv(1024)
print(result)
s.close()
