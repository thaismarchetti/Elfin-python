#!/usr/bin/env python3

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM, SOCK_STREAM
import sys
#PORT_NUMBER = 0
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '127.0.0.1' )
#hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_STREAM )
mySocket.bind( (hostName, PORT_NUMBER) )
mySocket.listen(5)

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

#SERVER_IP   = '169.254.229.243'
#PORT_NUMBER = 5000
#mySocket.connect((SERVER_IP, PORT_NUMBER))

while True:
    client, addr = mySocket.accept()
    (data,addr) = client.recvfrom(SIZE)
    data = data.decode('utf-8')
    cmd = data.split(',')[0]
    msg_return = cmd+",OK,;"

    client.sendall(msg_return.encode('utf-8'))
print('out')
sys.exit()
