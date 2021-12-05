#!usr/local/bin

import sys

lines = open(sys.argv[1])

x = 0
y = 0

for l in lines:
    (i, n) = l.split()
    n = int(n)
    i = i.strip()

    if i =='forward':
        x = x + n
    elif i =='down':
        y = y + n
    else:
        y = y - n


print  "{0}, {1}".format(x, y)

print x* y
