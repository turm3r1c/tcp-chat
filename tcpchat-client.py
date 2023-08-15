import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9876

client.connect((TARGET_IP, TARGET_PORT))

nickname = input("Choose your nickname: ")

def write():
    while True:
        message = input(f"")
        client.send(message.encode("ascii"))

def receive():
    while True:
        message = client.recv(1024).decode("ascii")
        if message == "Choose your nickname: ":
            client.send(nickname.encode("ascii"))
        else:
            print(message)

write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()