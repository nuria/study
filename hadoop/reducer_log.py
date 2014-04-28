#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the page name, counter is what we should add to the page totals
#
# All the hits for a particular page will be presented,
# then the key will change and we'll be dealing with the next page

total = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # key = page
    thisKey, count = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", total
        oldKey = thisKey;
        total = 0

    oldKey = thisKey
    total = total + int(count)

if oldKey != None:
    print oldKey, "\t", total

