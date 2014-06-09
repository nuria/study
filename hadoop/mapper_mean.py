#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# we want to print amount sold in each date of the week
# like 0 45.0 -> 45.0 sales for Monday, datetime module numerates days from 0 to 6
# reducer will come along and will add all items -> how does this work when you have multiple reducers?
# mmmm ... mean of means?

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)
