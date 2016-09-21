__author__ = 'Dixit_Patel'
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", 10000))
maxsize = 10000
while True:
    data, addr = s.recvfrom(maxsize)
    print "received ", data
    resp = "Get off my lawn!"
    s.sendto(resp, addr)