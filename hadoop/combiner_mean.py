#!/usr/bin/python

# Format of each line is:
# weekday,cost
#
# Note that for the mean function you can use a workaround for using combiners by
# using two separate reduce methods, a first one that would be used
# as the addition function (and thus that can be set as the combiner)
# that would emit the intermediate sum as the key and the number
# of addition involved as the value, and a second reduce function that would compute the mean
# by taking into account the number of addition involved

# combiner input key value and output key value need to be the same
# as they might run multiple times

import sys

# output will be weekday, addition of costs, number of items in addition
sales = {}

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 3:
        # Something has gone wrong. Skip this line.
        continue

    dayOfWeek, cost, n = data
    cost = float(cost)
    n = int(n)

    if sales.get(dayOfWeek) is None:
        sales[dayOfWeek] = (cost, n)
    else:
        prior_cost, prior_n = sales[dayOfWeek]
        cost = cost + prior_cost
        n = n + prior_n
        sales[dayOfWeek] = (cost, n)

print sales
for day in sales.keys():
    cost, n = sales[day]
    print "{0}\t{1}\t{2}".format(day, cost, n)
