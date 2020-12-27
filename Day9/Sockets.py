import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SOCKETS")
print(ascii_banner)

mes = input("\nType a message: ")
"""- choosing an socket, we will use Internet Socket here
- TCP or UPD?
- IP selection
- Port selection
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",55563))
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connecteddddd!\n".encode())
    client.send(mes.encode())
    client.close()

