#!usr/local/bin
import sys

lines = list(open(sys.argv[1].strip()))

lines = lines[0].strip()

print lines.split(',')

positions = map(lambda x: int(x), lines.split(','))

max_position = max(positions)

print positions

# need to decide what is the position to which they move with less budget 

# we can calculate all possibilities to start and likely this will not work for part 2

# 16,1,2,0,4,2,7,1,2,14

D  = {}
D = {key:0 for key in range(0, max_position+1)}

# for all possible points
for p in range(0, max_position +1):
    # calculate move per key
    # if you are it budget is 0
    budget = 0
    
    # for the items we have
    for i in positions:
        # challenge 1 budget = budget + abs(p-i)  
        budget = budget + abs(p-i) *(abs(p-i) +1)/2
            
    D[p] = budget 

print D

# now find key with smallest budget
_min =  float('inf')
#position
pos = None 

for p in range(0, max_position + 1 ):
    if D[p] <  _min:
        pos = p
        _min = D[p]

print "postion: {0} budget {1}".format(pos, D[pos])

