#!/usr/bin/python

import sys

airportTotal = 0
oldKey = None

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
        print oldKey, "\t", airportTotal
        oldKey = thisCountry  # Sets the value of oldKey with the first country name it encounters
        airportTotal = 0  # Resets the count when there is a change

    oldKey = thisCountry  # Country Name
    airportTotal += int(thisID)  # Adds 1 to the count of airports for that country name

if oldKey is not None:  # When reached EOF
    print oldKey, "\t", airportTotal  # Prints the final set of values

