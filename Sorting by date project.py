import urllib2
import json

url = "http://dev.c0l.in:8888/"

response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
sector3 = raw_input("Choose your Sector e.g Financial, Technology, Healthcare etc. ")
found = False
for record in data:
    if str(record["sector"]) == sector3:
        print record
        found = True
if found == False:
    print "Sector not found"
    
def sort_by_date(company):
    return company["fiscal_year_beginning"]

def sort_by_sector(company):
    return company["sector"]

sorted_data = sorted(data, key=sort_by_date)

for company in sorted_data:
    print company["company"]["name"] + str(company["fiscal_year_beginning"])
