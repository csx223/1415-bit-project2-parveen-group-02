import urllib2
import json

url = "http://dev.c0l.in:8888/"

response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
# Printing Data

# Asking whether to see all data
sector1 = raw_input("Do you wish to see all your sectors? y/n: ")
if sector1 == 'y':
    for x in data:
        print x["sector"]
elif sector1 == 'n':
    print "You have chosen not to view all sectors"
else:
    print "You have chosen not to view all sectors"

# Choosing Sector
sector3 = raw_input("Choose your Sector e.g Financial, Technology, Healthcare etc. ")
found = False
for record in data:
    if str(record["sector"]) == sector3:
        print record
        found = True
if found == False:
    print "Sector not found"

# Sorting all the companys of chosen sectors by Date:


# Choosing Specific Company ID
sector2 = raw_input("Choose your Company ID's: ")
found = False
for record in data:
    if str(record["id"]) == sector2:
        print record
        found = True
if found == False:
    print "ID not found"

# View Purchases of Chosen Company
sector2 = raw_input("What Company ID's purchases would you like to see: ")
found = False
for record in data:
    if str(record["id"]) == sector2:
        if str(record["purchases"]) ==sector2
        print record
        found = True
if found == False:
    print "ID not found"

# Save File as CSV








# Choosing Sector
#print "Sectors to choose: financial, etc."

#sector = raw_input("Choose your sector: ")
#if sector == 'healthcare':
 #   for x in data:
  #      print x["company"]

#elif sector == 'financial':
 #   for x in data:
 #       print x["company"]
#else:
 #   print "No Data"

#Print "Hello,Your Sector is %s." % sector
#What sector do you wish to continue with? to = data['sector']
#print to





