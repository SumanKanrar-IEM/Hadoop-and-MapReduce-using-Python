#!/usr/bin/python

import sys

airportTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the type, val is the counters(airports) of that type
#
# All the airports for a particular type will be presented,
# then the key will change and we'll be dealing with the next country

for line in sys.stdin:  # Reads the output given by the mapper script
    data_mapped = line.strip().split("\t")  # Takes each line and puts it into the "data_mapped" array.
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisType, thisID = data_mapped
    # Puts the values of each line to corresponding variables.

    if oldKey and oldKey != thisType:  # Checks if this is the first line of the data_mapped or any change of type
        print oldKey, "\t", airportTotal
        oldKey = thisType  # Sets the value of oldKey with the first type it encounters
        airportTotal = 0  # Resets the count when there is a change

    oldKey = thisType  # Type
    airportTotal += int(thisID)  # Adds 1 to the count of airports for that type of airport

if oldKey is not None:  # When reached EOF
    print oldKey, "\t", airportTotal  # Prints the final set of values

