import socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(("127.0.0.1", 1333))
while True:
    msg , addr = server_sock.recvfrom(1024)
    data = msg.decode("utf-8")
    server_sock.sendto(str.encode(data),addr)
server_sock.close()
