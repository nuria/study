#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202

# We want to count pageviews, thus we need to output "page\t1"
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    #page is the 7th item
    # ip is teh 1st item
    ip = data[0]
    # let's remove anything after "?"
    #page = url.split("?")[0]

    print "{0}\t{1}".format(ip,1)

