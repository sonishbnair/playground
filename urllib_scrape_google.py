import urllib2
req = urllib2.Request(url='https://www.google.com/#q=maywood',data='maywood')
f = urllib2.urlopen(req)
print f.read()
