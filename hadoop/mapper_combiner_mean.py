#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# we want to print amount sold in each date of the week
# like 0 45.0 -> 45.0 sales for Monday, datetime module numerates days from 0 to 6
# reducer will come along and will add all items -> how does this work when you have multiple reducers?
# this can only work if you have one reducer
# which will need to manipulate loads of data
# we will use combiners as an intermediate step
# http://www.philippeadjiman.com/blog/2010/01/14/hadoop-tutorial-series-issue-4-to-use-or-not-to-use-a-combiner/
# combiners will read <weekday>, <sum of costs>, <number of items in sum>

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        # on 1st swap of mapper there is only 1 item that went into
        # the total of costs
        print "{0}\t{1}\t{2}".format(weekday, cost, 1)
