#!/usr/bin/env python
import socket
import pickle

class myobject():
    def __init__(self,  list1,  list2):
        self.list1=list1
        self.list2=list2

# create a server
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1099))
server.listen(3)
while True:
    (client, address) = server.accept()
    msg=client.recv(1024)
    print "received data "
    x = pickle.loads(msg)
    x.list1.sort()
    x.list2.sort()
    msg= pickle.dumps(x)
    client.send(msg)
    
    
