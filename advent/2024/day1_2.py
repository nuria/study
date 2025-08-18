#! /opt/nflx/python

f = open('./input1.txt')

l1 = []
l2 = {}


for l in f:
    (item1, item2) = l.split()
    l1.append(int(item1))
    if l2.get(int(item2)) is None:
        l2[int(item2)] = 0
    l2[int(item2)] +=1

print (l2)
print (l2.get(l1[0]))

# similarity score
# adding up each number in the left list after multiplying it 
# by the number of times that number appears in the right list
s = 0

for n in l1:
    if l2.get(n) is not None:
        s = s + n * l2[n] 
        
print ("similarity: {0} ".format(s))







