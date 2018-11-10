#!/usr/bin/python

import sys

airportTotal = 0
oldKey = None
mydict = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the IDs for a particular country will be presented,
# then the key will change and we'll be dealing with the next country

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisAirport, thisID = data_mapped

    if oldKey and oldKey != thisAirport:
        mydict.update({ oldKey : airportTotal })
        oldKey = thisAirport;
        airportTotal = 0

    oldKey = thisAirport
    airportTotal += int(thisID)

if oldKey != None:
    mydict.update({ oldKey : airportTotal })
#    print max(mydict.items(), key=lambda k: k[1])
    maxCountry = max(mydict, key=mydict.get)
    print maxCountry	
    

