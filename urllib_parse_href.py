import urllib
from BeautifulSoup import *

count = 1
url = raw_input('Enter URL - ')
loop = int(raw_input('Enter count - '))
position = int(raw_input('Enter position - '))

while True:
    print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get('href', None)
    count += 1
    if count > loop:
        print tags[position-1].contents[0]
        break
