#!/usr/bin/env python
import socket
# create a server
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1080))
server.listen(3)
while True:
    (client, address) = server.accept()
    msg=client.recv(100)
    print "received ",  msg
    client.send("pong")
    
    
