from json import JSONEncoder
import socket
import sys

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

jsonString = JSONEncoder().encode({
  "actors": {
    "actor": [
      {
        "id": "1",
        "firstName": "Tom",
        "lastName": "Cruise"
      }
    ]
  }
})
print(type(jsonString))
s.connect((host, port))
s.send(jsonString)
result = s.recv(1024)
print(result)
s.close()
