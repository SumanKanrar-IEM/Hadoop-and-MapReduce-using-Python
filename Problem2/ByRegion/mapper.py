#!/usr/bin/python

# Format of each line is:
# "ID","TYPE","NAME","LATITUDE","LONGITUDE","COUNTRY","REGION"
#
# We want element 6 (REGION)
# We need to write it to standard output and counter(1) for each region, separated by a COMMA

import sys

for i,line in enumerate(sys.stdin):  # Reads from the input file
	if i == 0:  # Since 1st line are the headings. So we have to ignore that line
		continue
	else:
		data = line.strip().split(",")  # Takes each line and puts into "data" array
		if len(data) == 7:  # Checks if all the fields are there or not
			id, type, name, latitude, longitude, country, region = data
			# Puts the values of each line to corresponding variables.
			print "{0}\t{1}".format(region, 1)  # This will act as the input for the reducer
