import socket
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1222
client_sock.connect((host, port))
while True:
    inp= input("enter your echo message : ")
    client_sock.send(str.encode(inp))
    data=client_sock.recv(2048)
    print(data.decode("utf-8"))
client_sock.close()

