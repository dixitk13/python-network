__author__ = 'Dixit_Patel'
import socket
s = socket.socket()
s.connect(('localhost', 9000))
maxsize = 1000
fragments = [] # List of chunks
while True:
    chunk = s.recv(maxsize) # Get a chunk
    if not chunk:
        break # EOF. No more data
    fragments.append(chunk)
# Reassemble the message
message = "#".join(fragments)
print "=> ", message