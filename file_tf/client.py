import socket
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=1336
client_sock.connect((host,port))
file=open("sample_file.txt" , "rb")
while True:
    data=file.read(1024)
    client_sock.send(data)
file.close()
client_sock.close()
