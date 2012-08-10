ipaddr=raw_input(['Type the ip address of the server'])
#ip recive code
import socket
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect((ipaddr, 48500))
s.send('ping')
result = s.recv(256)
print result
s.close()
