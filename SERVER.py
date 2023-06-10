import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))

server.listen()
print('<<< SERVER IS LISTENING ... >>>')

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)


def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)

        except:
            index = clients.index(client)

            clients.remove(client)
            client.close()

            nickname = nicknames[index]
            broadcast(f'[ {nickname} ] <<< has left the chat >>>'.encode('ascii'))
            nicknames.remove(nickname)

            break


def receive():
    while True:
        client, address = server.accept()
        print(f'connected with {str(address)}')
        
        nickname = client.recv(1024).decode('ascii')
        
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'<<< Nickname of the client is [ {nickname} ] >>>')
        broadcast(f'<<< [ {nickname} ] joind the chat ! >>>'.encode('ascii'))
        
        client.send('<<< great your connected to the server ! >>>'.encode('ascii'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
