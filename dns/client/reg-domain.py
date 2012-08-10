import socket
dnsname='dnsname'#pick dns name
serverip='127.0.0.1'#pick server ip address
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverip, 1080))
ip=socket.gethostbyname(socket.gethostname())
s.send(ip)
s.send(dnsname)
result = s.recv(256)
print result
s.close()
