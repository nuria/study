#!usr/local/bin
import sys
import copy

lines = list(open(sys.argv[1]))

days = int(sys.argv[2])

print "days : {0}".format(days)

fish = lines[0].strip()


fish = fish.split(',')

fish = map(lambda x: int(x), fish)

print fish

valid_sequence_first = [8, 7, 6, 5, 4, 3, 2, 1, 0]

valid_sequence = [6, 5, 4, 3, 2, 1, 0]


day = 0

# transition from 0 ->6
# initial spawn at 8 
keys = [0,1,2,3,4,5,6,7,8]

D = {key: 0 for key in keys}


# bootstrap 
for f in fish:
    D[f] = D[f] + 1

print D.items()


while (day <days):
    
    D_mask = {key:0 for key in keys}
    
    for k in D.keys():
        if k >=1:
            D_mask[k] = D_mask[k] + (-1) * copy.copy(D[k])
            D_mask[k-1] =  D_mask[k-1] + copy.copy(D[k])
        if k == 0:
            D_mask[0] = D_mask[0] + (-1) * copy.copy(D[0])
            D_mask[8] = D_mask[8] + copy.copy(D[0])
            D_mask[6] = D_mask[6] + copy.copy(D[0])

    # now apply mask 

    for k in D.keys():
        D[k] = D[k] + D_mask[k] 

    day = day + 1
    #print "day: {0}, D: {1}".format(day, map(lambda x: x, D.items()))

total = 0

for k in D.keys():
    total = total + D[k]

print "total: {0}".format(total)




