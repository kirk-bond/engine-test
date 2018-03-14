import json
import socketserver


class SocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(self.data)
        try:
            json.loads(self.data.decode())
        except Exception as e:
            invalid = "Invalid JSON format: %s" % e
            print(invalid)
            self.request.sendall(invalid.encode())
        else:
            valid = "Received valid flag input %s" % self.data
            self.request.sendall(valid.encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 5555
    server = socketserver.TCPServer((HOST, PORT), SocketServer)
    server.serve_forever()