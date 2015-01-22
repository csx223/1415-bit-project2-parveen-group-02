import urllib2
import json

url = "http://dev.c0l.in:8888/"

response = urllib2.urlopen(url).read()

data = json.loads(response.decode('utf8'))

# sales highest to lowest 
#sector3 = raw_input("Choose which sector sales you are intrested in, results will be shown highest to lowest ")
sector3 = raw_input("Choose your Sector e.g Financial, Technology, Healthcare etc. ")

found = False
filter_data=[]
for record in data:
    if str(record["sector"]) == sector3:
        print record
        found = True

print filter_data
if found == False:
    print "Sector not found"

def sort_by_sales(company):
    return company["company"]["sales"]

sorted_data = sorted(filter_data, key=sort_by_sales, reverse=True)

print sorted_data 
