import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1333

client_sock.connect((host, port))

print("Connected to Server")

while True:

    command = input("Enter Command: ")

    client_sock.send(command.encode("utf-8"))

    if command.lower() == "exit":
        break

    data = client_sock.recv(1024)

    print("Server:", data.decode("utf-8"))

client_sock.close()