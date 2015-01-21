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

import csv

with open('thefile.csv', 'rb') as f:
    data = list (csv.reader(f))

    import collections
    counter = collections.defaultdict(int)
    for row in data:
        counter[row[0]]+=1

        writer = csv.writer(open("/path/to/my/file", 'w'))
        for row in data :
            if counter[row[0]] >=4:
                writer.writerow(row) 
