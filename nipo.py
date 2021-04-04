import conn

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
    sock = conn.NipoSocket()

def OpenConnection( ): 
    CreateConnection()
    sock.connect(conf.server, conf.port)

def Ping():  
    OpenConnection()
    string = conf.token+" "+"ping"
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def Status():
    OpenConnection()
    string = conf.token+" "+"status"
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode(), ok)

def Set(key, value):
    OpenConnection()
    string = conf.token+" set "+key+" "+value
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def Get(key):
    OpenConnection()
    string = conf.token+" get "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def Select(key):
    OpenConnection()
    string = conf.token+" select "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def Avg(key):
    OpenConnection()
    string = conf.token+" avg "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def Sum(key):
    OpenConnection()
    string = conf.token+" sum "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def Count(key):
    OpenConnection()
    string = conf.token+" count "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

