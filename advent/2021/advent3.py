#!usr/local/bin

lines = open('./input3.txt')



lines = map(lambda x:x.strip(), lines)

total = len(lines)

print lines
print len(lines[0])


def most_popular(i):
    tally = 0
    for l in lines:
        tally = tally + int(l[i])

    if tally > total/2:
        return '1'
    else:
        return '0'

gamma=''

epsilon =''


for i in range(0, len(lines[0])):
    most = most_popular(i)
    gamma = gamma + most
    if most== '1':
        least_popular = '0'
    else:
        least_popular = '1'
    
    epsilon= epsilon + least_popular


print gamma
print epsilon

print int(gamma,2) *int(epsilon,2)
