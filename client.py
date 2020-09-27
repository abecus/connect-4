import threading
import socket


# host = '8.210.143.41'
host = '127.0.0.1'
port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while 1:
        try:
            massage = client.recv(1024).decode('ascii')
            print(massage, end='\n')
        except:
            print('error occurred')

def send():
    while 1:
        massage = input()
        client.send(massage.encode("ascii"))

    
recvThread = threading.Thread(target=receive)
recvThread.start()

writeThread = threading.Thread(target=send)
writeThread.start()