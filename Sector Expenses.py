import urllib2
import json

url = "http://dev.c0l.in:8888/"

response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

# Specific Sectors Purchases:
purchases = raw_input("which Sector purchases would you like to view?: ")
found = False
for record in data:
    if str(record["sector"]) == purchases:
        print record["company"]["name"]
        print record["company"]["expenses"]
        
        
