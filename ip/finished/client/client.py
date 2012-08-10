#!/usr/bin/env python
import socket
ipaddr=raw_input(['Type the ip address of the server'])#use if ip change
#ip recive code
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipaddr, 48500))
s.send(socket.gethostbyname(socket.getfqdn()))
result = s.recv(256)
print result
s.close()
# create a server
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 65534))
server.listen(3)
while True:
    (client, address) = server.accept()
    msg=client.recv(4096)
    print "received ",  msg
    client.send(result)
