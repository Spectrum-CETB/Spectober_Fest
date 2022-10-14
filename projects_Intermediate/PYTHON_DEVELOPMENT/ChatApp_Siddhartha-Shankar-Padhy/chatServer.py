import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
clients = []
usernames = []

def handle(client):
    connected = True
    while connected:
        try:
            message = client.recv(1024)
            message = message.decode(FORMAT)
            if message == '$$PARTICIPANTS$$':
                send_list = str(usernames)
                client.send(send_list.encode(FORMAT))
            else:
                message = message.encode(FORMAT)
                broadcast_msg(message, client)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast_msg((f'{username} left the chat!'.rjust(35,'-').encode(FORMAT)), client)
            usernames.remove(username)
            break

def broadcast_msg(message, spec_client):
    try:
        if spec_client in clients:
            for client in clients:
                if client != spec_client:
                    complete_msg = message.decode(FORMAT)
                    client.send(complete_msg.encode(FORMAT))
        else:
            for client in clients:
                client.send(message)
    except Exception as e:
        print(f'Error while broadcasting: {e}')

def receive():
    while True:
        client, addr = server.accept()
        print(f'[CONNECTED TO {str(addr)}]')
        clients.append(client)

        client.send('USER'.encode(FORMAT))
        username = client.recv(1024).decode(FORMAT)
        usernames.append(username)
        print(f'{addr}: {username}')

        joining_msg = f'{username} joined the chat!'
        joining_msg = joining_msg.rjust(35, '-').encode(FORMAT)
        broadcast_msg(joining_msg,client)
        client.send('Connected to the server!'.rjust(36,'-').encode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("SERVER is running...")
receive()