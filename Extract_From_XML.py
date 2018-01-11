import urllib
import xml.etree.ElementTree as ET

serviceURL = 'http://python-data.dr-chuck.net/comments_214552.xml'

data =  urllib.urlopen(serviceURL).read()
tree = ET.fromstring(data)
totalCount = 0

for count in tree.findall('.//count'):
    totalCount += int(count.text)

# WORKING BLOCK Below
# for eachCount in tree.iter('count'):
#     totalCount += int(eachCount.text)

print "Total Count: ", totalCount
