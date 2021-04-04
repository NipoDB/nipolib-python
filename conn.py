import socket

class NipoSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        msg = msg+"\n"
        self.sock.sendall(msg.encode())
        response = self.sock.recv(1024)
        if response != None :
            return response 
            
    def close(self):
        self.sock.close()

