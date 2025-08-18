#! /opt/nflx/python

f = open('./input1.txt')

l1 = []
l2 = []

# use two lists, sort them
# add distance

for l in f:
    (item1, item2) = l.split()
    l1.append(int(item1))
    l2.append(int(item2))


l1.sort()
l2.sort()

print ("smallest")

print(l1[0])
print(l2[0])

d= 0

for i in range(0, len(l1)):
    d = d + abs(l1[i]- l2[i])

print ("distance: {0} ".format(d))







