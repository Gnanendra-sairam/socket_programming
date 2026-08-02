import socket
import threading

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1333

server_sock.bind((host, port))
server_sock.listen(5)

print("Server is waiting for clients...")

database = {}

def client(connection):
    while True:
        data = connection.recv(1024)

        if not data:
            break

        command = data.decode("utf-8")

        if command.lower() == "exit":
            break

        parts = command.split()

        if len(parts) == 0:
            connection.send("Invalid Command".encode("utf-8"))
            continue

        operation = parts[0].upper()

        if operation == "PUT":
            if len(parts) != 3:
                connection.send("Usage: PUT key value".encode("utf-8"))
            else:
                key = parts[1]
                value = parts[2]
                database[key] = value
                connection.send("Stored Successfully".encode("utf-8"))

        elif operation == "GET":
            if len(parts) != 2:
                connection.send("Usage: GET key".encode("utf-8"))
            else:
                key = parts[1]
                if key in database:
                    connection.send(database[key].encode("utf-8"))
                else:
                    connection.send("Key Not Found".encode("utf-8"))

        elif operation == "DELETE":
            if len(parts) != 2:
                connection.send("Usage: DELETE key".encode("utf-8"))
            else:
                key = parts[1]
                if key in database:
                    del database[key]
                    connection.send("Deleted Successfully".encode("utf-8"))
                else:
                    connection.send("Key Not Found".encode("utf-8"))

        else:
            connection.send("Invalid Command".encode("utf-8"))

    connection.close()

while True:
    client_sock, addr = server_sock.accept()
    print(f"Connected to {addr}")

    t = threading.Thread(target=client, args=(client_sock,))
    t.start()
