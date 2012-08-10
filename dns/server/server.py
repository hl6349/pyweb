#!/usr/bin/env python
import socket
# make vars
main=[]
count=0
search=0
totalrecords=0
totalstrings=0
# create a server
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1088))
server.listen(3)
while True:
    (client, address) = server.accept()
    ipaddr=client.recv(4096)
    domain=client.recv(4096)
    main.append(ipaddr)
    count=count+1
    main.append(domain)
    count=count+1
    print "new record ",  ipaddr, '=', domain
    client.send('Your DNS is:', domain)
    totalstrings=count
    totalrecords=count/2
    
