__author__ = 'Dixit_Patel'
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
# s.listen(backlog) => backlog is # of pending connections to allow
s.listen(5)
print "Started, Acceptiing Connections!"
while True:
    c, a = s.accept()
    print "Received connection from", a
    c.send("Hello %s\n" % a[0])
    for i in range(0, 100):
        c.send("message")
    c.send('')
    c.close()