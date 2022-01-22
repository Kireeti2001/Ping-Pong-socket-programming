import socket
c = socket.socket()
c.connect(('localhost', 12345))
input_string = input("Type the message:")
c.send(bytes(input_string,'utf-8'))
if input_string == "Ping":
    print("Pong")

else:
    print("Dropped")
c.recv(1024).decode()
c.close()