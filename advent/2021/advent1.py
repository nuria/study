#!usr/local/bin/python

import sys

lines = open(sys.argv[1])

lines = map(lambda x: int(x), lines)

prior = lines[0]
txt = ''
for i in range(1, len(lines)):
    height = lines[i] -prior
    if height > 0:
        txt = 'increased'
    else:
        txt ='decreased'
    prior = lines[i]
    print "{0} {1}".format(lines[i], txt)





print "hola"


