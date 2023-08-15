import socket
import threading

IP = "127.0.0.1"
PORT = 9876

client_list = []
nickname_list = []

# Initiate server socket object, bind, and constantly listen for clients
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
print(f"--- Listening on {IP}:{PORT}.")

# Function for broadcasting like a chatroom; make sure message is encoded in bytes
def broadcast(message):
    for client in client_list:
        client.send(message)

# Function for handling messages of clients once they are connected to the server
def handle(client, nickname):
    while True:
        message = client.recv(1024).decode("ascii")
        message = f"{nickname}: {message}"
        broadcast(message.encode("ascii"))

# Main function calling all other functions
def main():
    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]} : {address[1]}")
        
        client.send(f"Choose your nickname: ".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nickname_list.append(nickname)
        print(f"The client has chosen the nickname: {nickname}")
        broadcast(f"{nickname} has joined the chat.".encode("ascii"))

        client_list.append(client)
        
        thread = threading.Thread(target=handle, args=(client,nickname))
        thread.start()


if __name__ == "__main__":
    main()