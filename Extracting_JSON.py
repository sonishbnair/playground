import urllib
import json

serviceURL  = raw_input("Service URL:")
data =  json.loads(urllib.urlopen(serviceURL).read())

count = 0
for item in data['comments']:
    count += int(item['count'])

print "Total Count:", count
