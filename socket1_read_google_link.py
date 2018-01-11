import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Before CONNECTION-----"
try:
    mysock.connect(('www.google.com', 80))
    mysock.send('GET https://www.google.com/#q=maywood HTTP/1.0\n\n')
except:
    print "Error in socket connection"

print "After CONNECTION-----"
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data . "---------------------------------------";

mysock.close()
