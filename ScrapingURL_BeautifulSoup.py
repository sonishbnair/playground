import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_214555.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

sumOfNumbers = 0
tags = soup('span')
for tag in tags:
    sumOfNumbers += int(tag.contents[0])

print "Sum of number is: ", sumOfNumbers;
