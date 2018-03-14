import socket
import sys

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])
userinput = sys.argv[3]

s.connect((host, port))
s.send(userinput.encode())
result = s.recv(1024)
print(result)
s.close()
