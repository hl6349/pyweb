#!/usr/bin/env python
import socket

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 65534))
s.send("ping")
result = s.recv(256)
print("Local address:"+result)
s.close()
