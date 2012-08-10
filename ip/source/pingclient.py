import socket

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1080))
s.send("ping")
result = s.recv(256)
print result
s.close()
