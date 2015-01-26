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
sector2 = raw_input("Choose your Sector e.g financial, technology, healthcare etc. ")
found = False
for record in data:
    if str(record["sector"]) == sector2:
        print record
        found = True
if found == False:
    print "Sector not found"

# Specific Sectors Purchases:
purchases = raw_input("which Sector purchases would you like to view?: ")
found = False
for record in data:

    if str(record["sector"]) == purchases:
        print record["company"]["name"]
        print record["company"]["purchases"]


# Specific Sectors Purchases:
purchases = raw_input("which Sector expenses would you like to view?: ")
found = False
for record in data:

    if str(record["sector"]) == purchases:
        print record["company"]["name"]
        print record["company"]["expenses"]


# Sorting all the companys of chosen sectors by Date:
sector3 = raw_input("Choose which sectors companys you would like to view by date e.g financial, technology, healthcare etc. ")
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

# sales highest to lowest 
#sector3 = raw_input("Choose which sector sales you are intrested in, results will be shown highest to lowest ")
sector4 = raw_input("Choose which Sectors sales from highest to lowest, you would like to view e.g financial, technology, healthcare etc. ")

found = False
filter_data=[]
for record in data:
    if str(record["sector"]) == sector4:
        filter_data.append(record)
        found = True
    
if found == False:
    print "Sector not found"

def sort_by_sales(company):
    return company["company"]["sales"]

sorted_data = sorted(filter_data, key=sort_by_sales, reverse=True)

#print sorted_data
for company in sorted_data:
    #print company["company"]["name"] + str("company" "sales"])
    print company["company"]["name"], "\t" + str(company["company"]["sales"])

# Choosing Specific Company ID
sector2 = raw_input("Choose your Company ID's: ")
found = False
for record in data:
    if str(record["id"]) == sector2:
        print record
        found = True
if found == False:
    print "ID not found"


# working out GPM
print "Equation to work out Gross Profit Margin Sales is = Sales Revenue - Cost of Sales."
GrossProfitMargin = raw_input("which Sector Gross Profit Margin would you like to view?: ")
found = False
for record in data:
    if str(record["sector"]) == GrossProfitMargin:
        name = (record["company"]["name"])
        print name
        sales = float(record["company"]["sales"])
        #print sales 
        #print record["company"]["sales"]
        purchases = float(record["company"]["purchases"])
        #print purchases
        opening_stock = float(record["company"]["opening_stock"])
        #print opening_stock
        closing_stock = float(record["company"]["closing_stock"])
        #print closing_stock

        #print record["company"]["purchases"]
        #print record["company"]["sales"]
        gpm = (opening_stock + purchases - closing_stock) - sales
        print gpm
        csvfile.write( str(gpm)+","+str(sales)+","+str(purchases)+"\n" )
        print "*************************"

# Choosing Specific Company ID
sector2 = raw_input("Choose your Company ID's: ")
found = False
for record in data:
    if str(record["id"]) == sector2:
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





