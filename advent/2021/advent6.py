#!usr/local/bin
import sys

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

while (day < days):
    # loop through all the fish
    # and transition teh ones that need to be transitioning
    tmp_fish = []
    spawn = 0
    for f in fish:
        if f  >= 1:
            tmp_fish.append(f -1)
        elif f == 0:
            tmp_fish.append(6)
            spawn = spawn + 1 

    for i in range(0, spawn):
        tmp_fish.append(8)

    # copy list 
    fish = tmp_fish[:]
    day = day + 1
    #print "day: {0}, :{1}".format(day, fish)


#print "days: {0}, fish :{1}, len fish : {2}".format(days, fish, len(fish))

print len(fish)

