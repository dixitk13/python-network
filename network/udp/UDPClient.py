__author__ = 'Dixit_Patel'
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
maxsize = 10000
msg = "Hello World"
s.sendto(msg, ("localhost", 10000))
data, addr = s.recvfrom(maxsize)
print "received from client: ", data