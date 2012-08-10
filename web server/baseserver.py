#!/usr/bin/env python
#####################################
#	Set variables here				#
#####################################
doc="index.html"#Default document
port=80#Port
#####################################
#	Definitions done				#
#####################################
import socket
htmlo = file(doc)
html = htmlo.read()
htmlo.close()
# create a server
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", port))
server.listen(3)
while True:
	(client, address) = server.accept()
	msg=client.recv(4096)
	print msg
	client.send("<!DOCTYPE html>") 
	client.send(html)
	
    
    