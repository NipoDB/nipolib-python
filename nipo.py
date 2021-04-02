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
            print (repr(response))
            
    def close(self):
        self.sock.close()

class Config():
    def __init__(self, token, server, port):
        self.token = token
        self.server = server
        self.port = port

def CreateConfig(token, server, port):
    global conf
    conf = Config(token, server, port )

def CreateConnection() :
    global sock
    sock = NipoSocket()

def OpenConnection( ): 
    CreateConnection()
    sock.connect(conf.server, conf.port)

def Ping():    
    OpenConnection()
    string = conf.token+" "+"ping"
    sock.send(string)
    sock.close()

def Status():
    OpenConnection()
    string = conf.token+" "+"status"
    sock.send(string)
    sock.close()

def Set(key, value):
    OpenConnection()
    string = conf.token+" set "+key+" "+value
    sock.send(string)
    sock.close()

def Get(key):
    OpenConnection()
    string = conf.token+" get "+key
    sock.send(string)
    sock.close()

def Select(key):
    OpenConnection()
    string = conf.token+" Select "+key
    sock.send(string)
    sock.close()

def Avg(key):
    OpenConnection()
    string = conf.token+" avg "+key
    sock.send(string)
    sock.close()

def Sum(key):
    OpenConnection()
    string = conf.token+" sum "+key
    sock.send(string)
    sock.close()

def Count(key):
    OpenConnection()
    string = conf.token+" count "+key
    sock.send(string)
    sock.close()

