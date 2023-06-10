import socket
import threading

nickname = input("< CHOOSE A NICKNAME >")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
temp = 1


def recive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print("< AN ERROR OCCURRED ! >")
            client.close()
            break


def write(temp):
    while True:
        if temp == 1:
            client.send(nickname.encode('ascii'))
            temp = 0
        else:
            message = f' > {nickname} : {input("")}'
            client.send(message.encode('ascii'))


recevie_thread = threading.Thread(target=recive)
recevie_thread.start()

write_thread = threading.Thread(target=write, args=(temp,))
write_thread.start()
