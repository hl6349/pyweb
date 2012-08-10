#!/usr/bin/env python
import socket
# create a server
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1088))
server.listen(3)
while True:
    (client, address) = server.accept()
    msg=client.recv(4096)
    print "received ",  msg
    client.send("<h1>This is a test!!!</h1>")
    
    
