import socket
import threading


server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1111
server_sock.bind((host,port))
server_sock.listen(5)
print("waiting for connection")

def client(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break

        print(data.decode("utf-8"))
        
        
    connection.close()
while True:
    client_sock, addr =server_sock.accept()
    threading.Thread(target=client, args=(client_sock,)).start()
    
server_sock.close()

