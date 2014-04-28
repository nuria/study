#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the items for a particular key will be presented,
# then the key will change and we'll be dealing with the next key

total = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", total
        oldKey = thisKey;
        total = 0

    oldKey = thisKey
    total += float(thisValue)

if oldKey != None:
    print oldKey, "\t", total

