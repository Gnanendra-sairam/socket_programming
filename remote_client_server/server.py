import socket
import threading

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1233

server_sock.bind((host, port))
server_sock.listen(5)

print("Server started...")
print("Waiting for client...")

def client(connection):
    while True:
        command = input("Enter command: ")

        connection.send(command.encode("utf-8"))

        if command.lower() == "exit":
            break

        data = connection.recv(4096)

        if not data:
            break

        print(data.decode("utf-8"))

    connection.close()

while True:
    client_sock, addr = server_sock.accept()
    print(f"Connected to {addr}")

    t = threading.Thread(target=client, args=(client_sock,))
    t.start()
