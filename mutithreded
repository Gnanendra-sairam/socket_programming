import socket
import _thread
server_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1233
thread_count = 0

try:
    server_sock.bind((host,port))
except socket.error as er:
    print(str(er))
server_sock.listen(5)
print("server is waiting for connection")

def client_thread(connection):
    connection.send(str.encode("welcome to server"))
    while True:
        data1 = connection.recv(2048)
        if not data1:
            break
        print(data1.decode("utf-8"))
        connection.sendall(str.encode("lol"))
    connection.close()








while True:
    clint_sock,addr=server_sock.accept()
    print(f"connected to {addr[0]} {addr[1]}")
    _thread.start_new_thread(client_thread,(clint_sock,))
    thread_count+=1
    print("ThreadNumber"+str(thread_count))

server_sock.close()









