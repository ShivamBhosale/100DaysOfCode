import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",55563))

message = s.recv(2048) #Bytes of the message
s.close()
print(message.decode())
