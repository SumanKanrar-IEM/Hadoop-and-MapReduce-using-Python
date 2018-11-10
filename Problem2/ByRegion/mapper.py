#!/usr/bin/python

# Format of each line is:
# "ID","TYPE","NAME","LATITUDE","LONGITUDE","COUNTRY","REGION"
#
# We want elements 1 (ID) and 6 (COUNTRY)
# We need to write them out to standard output, separated by a COMMA

import sys

for i,line in enumerate(sys.stdin):
    if i == 0:
	continue
    else:
	data = line.strip().split(",")
	if len(data) == 7:
	    id, type, name, latitude, longitude, country, region = data
	    print "{0}\t{1}".format(region, 1)
