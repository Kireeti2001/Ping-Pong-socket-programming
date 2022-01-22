import socket
s = socket.socket()
print('Socket Created')
s.bind(('localhost', 12345))
s.listen(3)
print('Waiting for connection')
while True:
    c, addr = s.accept()
    print('Connected with', addr)
    input_string = c.recv(1024).decode()
    if not input_string:
        break
    print("From connected user: " + str(input_string))
    input_string = input(' -> ')
    if input_string == "Ping":
        c.send(input_string.encode())
    else:
        break
c.close()