import socket
import random
import pickle

class myobject():
    def __init__(self,  list1,  list2):
        self.list1=list1
        self.list2=list2
x  = myobject([1, 2, 3, 9, 4, 6, 7, 8, 5],  ['a','g', 'c', 'b', 'f', 'e','d'])
print x.list1
print x.list2
msg= pickle.dumps(x)
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1099))
s.send(msg)
result = s.recv(1024)

x = pickle.loads(result)
print x.list1
print x.list2
s.close()
