import socket
import threading
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1231
client_socket.connect((host,port))
def send():
    while True:
        msg = input("enter the msg you want to share with other clients : ")
        data = str(msg).encode("utf-8")
        client_socket.send(data)
def recv():
    while True:
        lol=client_socket.recv(2048)
        print(lol.decode("utf-8"))

t=threading.Thread(target=send)
t.start()
l=threading.Thread(target=recv)
l.start()

