import socket
import time
import threading

client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1111
client_sock.connect((host,port))

def server():
    while True:
        client_sock.send(str("heartbeat").encode("utf-8"))
        print("heartbeat send")
        time.sleep(5)

hh=threading.Thread(target=server)
hh.start()
hh.join()

while True:
    pass
