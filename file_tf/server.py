import socket
server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1336
server_sock.bind((host,port))
server_sock.listen(5)
print("waiting for the client")
client_sock, addr = server_sock.accept()
file = open("lol.txt", "wb")
while True:
    data=client_sock.recv(1024)
    file.write(data)
file.close()
client_sock.close()
server_sock.close()
