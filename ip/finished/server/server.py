#!/usr/bin/env python
#import statements here
import socket
import random
#set everything here
ipaddr=socket.gethostbyname(socket.getfqdn()) #ip address located
ipstr='0.0.0.0' #DO NOT CHANGE
port=48500
count=0
iplist=['','']
msg=''#THIS RESETS SERVER
#webserver code static
server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ipaddr, port))
server.listen(3)
#generate first ip (init. code).
ipvar1=1000
ipvar2=1000
ipvar3=1000
ipvar4=1000
portstr=str(port)
#say where to connect
print("Server is running at ip "+ ipaddr + " and port # " + portstr) 
#ip assign starts here. It is infinite loop.
while True:
    if not (msg == ''):
        if (ipvar1 > 0):
            ipvar1=ipvar1 - 1
            
        else:
            ipvar1=1000
            if (ipvar2 > 0):
                ipvar2=ipvar2 - 1
                
            else:
                ipvar2=1000
                if (ipvar3 > 0):
                    ipvar3=ipvar3 - 1
                    
                else:
                    ipvar3=1000
                    if (ipvar4 > 0):
                        ipvar4=ipvar4 - 1



    

    msg=''

    (client, address) = server.accept()#listen for client
    msg=client.recv(4096)#get signal from client
    print('ip:',  msg)#print sent output for debugging purposes
    ipstr1=str(ipvar1)#string each part of ip
    ipstr2=str(ipvar2)#string each part of ip
    ipstr3=str(ipvar3)#string each part of ip
    ipstr4=str(ipvar4)#string each part of ip
    ipvar=ipstr4 + '.' + ipstr3 + '.' + ipstr2 + '.' + ipstr1#make ip address
    iplist[count]=ipvar
    count=count+1
    iplist[count]=msg
    count=count+1
    client.send(ipvar)#send ip code
    
