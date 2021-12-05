#!usr/local/bin/python

import sys

lines = open(sys.argv[1])

lines = map(lambda x: int(x), lines)

# calculate and print three sums
s0 = sum(lines[0:3])
l = len(lines)

print s0

for i in range(1, len(lines)):
    if i + 3 <=len(lines):
        s = sum(lines[i:i+3])
        print s







