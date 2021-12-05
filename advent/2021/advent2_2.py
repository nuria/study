#!usr/local/bin

import sys

lines = open(sys.argv[1])

x = 0
y = 0
aim = 0

for l in lines:
    (i, n) = l.split()
    n = int(n)
    i = i.strip()

    if i =='forward':
        x = x + n
        y = y + aim * n
    elif i =='down':
        #y = y + n
        aim = aim + n
    else:
        #y = y - n
        aim = aim -n
    #print " {0} {1} {2}".format(x, y , aim)

print  "{0}, {1}".format(x, y)

print x* y
