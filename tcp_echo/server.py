import socket
server_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="127.0.0.1"
port=1222
server_sock.bind((host,port))
server_sock.listen(5)
print("server is waiting for connection")
while True:
    client_sock,addr=server_sock.accept()
    while True:
        data=client_sock.recv(2048)
        if not data:
            break
        ll=data.decode("utf-8")
        client_sock.send(str.encode(ll))
    client_sock.close()
    
