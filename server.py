import threading
import socket
from board import Board

host = ''
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = dict()

player = {1:'Red', 0:'Yellow'}


def handle(client):
	while 1:
		try:
			s = client.recv(1024).decode('ascii')
			print(s)
			if s:
				if clients[client][1] == 0 and s == "START":
					client.send('\nREADY'.encode("ascii"))
					client.send(f"\nPlayer {player[clients[client][0].turn]} Turn".encode('ascii'))
					clients[client][1] = 1
					continue
					
				if clients[client][1] == 0:
					continue
				
				game = clients[client][0]
				if s.isdigit():
					out = game.drop(int(s))
					if out != False:
						client.send(f"{game}".encode('ascii'))

						if out == True:
							client.send('\nValid Move'.encode('ascii'))
						else:
							client.send(f"\n{out}".encode('ascii'))
					else:
						client.send('\nInvalid Move'.encode('ascii'))
						continue

					client.send(f"\nPlayer {player[game.turn]} Turn".encode('ascii'))

				elif clients[client][1] == 1 and s == "START":
					client.send('READY'.encode('ascii'))
					game.reset()
					client.send(f"\nPlayer {player[game.turn]} Turn".encode('ascii'))


		except:
		    client.close()
		    del clients[client]
		    print(f"{client} left the chat")
		    break


def receive():
	while 1:
		try:
			client, add = server.accept()
			print(f"connected with {add}")
			game = Board()
			clients[client] = [game, 0]

			client.send("connected to the sever".encode("ascii"))
			client.send('\nType "START", for a new game.'.encode("ascii"))

			thread = threading.Thread(target=handle, args=(client,))
			thread.start()
		except:
			pass


print("Server Listening...")
receive()