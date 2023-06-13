import conn

class Config():
    def __init__(self, token, server, port):
        self.token = token
        self.server = server
        self.port = port

def create_config(token, server, port):
    global conf
    conf = Config(token, server, port )
    

def create_connection() :
    global sock
    sock = conn.NipoSocket()

def open_connection( ): 
    create_config()
    sock.connect(conf.server, conf.port)

def ping():  
    open_connection()
    string = conf.token+" "+"ping"
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def status():
    open_connection()
    string = conf.token+" "+"status"
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode(), ok)

def set(key, value):
    open_connection()
    string = conf.token+" set "+key+" "+value
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def get(key):
    open_connection()
    string = conf.token+" get "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def select(key):
    open_connection()
    string = conf.token+" select "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def avg(key):
    open_connection()
    string = conf.token+" avg "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def sum(key):
    open_connection()
    string = conf.token+" sum "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)

def count(key):
    open_connection()
    string = conf.token+" count "+key
    connection = sock.send(string)
    ok = False
    if connection:
        ok = True
    sock.close()
    return(connection.decode() , ok)
