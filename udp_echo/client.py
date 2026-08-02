import socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#client_sock.connect(("127.0.0.1",1333))
while True:
    msg = input("enter the echo message: ")
    client_sock.sendto(str.encode(msg), ("127.0.0.1",1333))
    txt,addr= client_sock.recvfrom(1024)
    print(txt.decode("utf-8"))
client_sock.close()

    
