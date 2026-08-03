import socket
import threading
server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1231
server_sock.bind((host,port))
server_sock.listen(5)
print("server is waiting for connection")
client = []
def brodcast(sender,message):
    if sender in client:
        for clients in client:
            if clients != sender:
                clients.send(str(message).encode("utf-8"))
    else:
        print("clint is not connected")

    
def client_function(connection):
    while True:
        data=connection.recv(2048)
        if not data:
            break 
        print(data.decode("utf-8"))
        msg = data.decode("utf-8")
        brodcast(connection,msg)
    



    
while True:
    client_server, addr = server_sock.accept()
    client.append(client_server)
    t=threading.Thread(target=client_function, args=(client_server,))
    t.start()
server_sock.close()
