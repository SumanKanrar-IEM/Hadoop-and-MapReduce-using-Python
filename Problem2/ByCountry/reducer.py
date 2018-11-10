#!/usr/bin/python

import sys

airportTotal = 0
oldKey = None
mydict = {}  # Declares and empty dictionary

# Loop around the data
# It will be in the format key\tval
# Where key is the country name, val is the counters(airports) in that country.
#
# All the counters(no of airports) for a particular country will be presented,
# then the key will change and we'll be dealing with the next country

for line in sys.stdin:  # Reads the output given by the mapper script
    data_mapped = line.strip().split("\t")  # Takes each line and puts it into the "data_mapped" array.
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisCountry, thisID = data_mapped
    # Puts the values of each line to corresponding variables.

    if oldKey and oldKey != thisCountry:  # Checks if this is the first line of the data_mapped or any change of country name
        mydict.update({oldKey: airportTotal})  # Adds the country name and total airports for that country in the form of  key:value in to the dictionary
        oldKey = thisCountry  # Sets the value of oldKey with the first country name it encounters
        airportTotal = 0  # Resets the count when there is a change

    oldKey = thisCountry  # Country Name
    airportTotal += int(thisID)  # Adds 1 to the count of airports for that country name

if oldKey is not None:  # When reached EOF
    mydict.update({oldKey: airportTotal})  # Adds the final set of values to the dictionary
#    print max(mydict.items(), key=lambda k: k[1])
    maxCountry = max(mydict, key=mydict.get)  # Gets the key of the maximum value ( country with maximum airports)
    print maxCountry  # Prints the country with maximum airports
    

