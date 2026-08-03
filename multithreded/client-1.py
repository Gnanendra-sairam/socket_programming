import socket
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1233
print("waiting for connection")
try:
    client_sock.connect((host,port))
except socket.error as er:
    print(er)

data=client_sock.recv(2048)
print(data.decode("utf-8"))
while True:
    input=input("enter the data to send")
    client_sock.send(str.encode(input))
    data1=client_sock.recv(2048)
    print(data1.decode("utf-8"))
client_sock.close()
