import socket

HOST = 'SERVER_IP'
PROT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PROT))

message = "Hello server" #set your message

socket.send(message.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))