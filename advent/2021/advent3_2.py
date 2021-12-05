#!usr/local/bin
import sys

lines = open(sys.argv[1])

lines = map(lambda x:x.strip(), lines)

total = len(lines)

def most_popular(i, _set):
    total = len (_set)
    tally = 0
    for l in _set:
        tally = tally + int(l[i])
    if tally > total/2.0:
        return '1'
    elif tally == total/2.0:
            return '1'
    else:
        return '0'


def least_popular(i, _set):
    total = len(_set)
    tally = 0
    for l in _set:
        tally = tally + int(l[i])

    if tally > total/2.0:
        return '0'
    elif tally == total/2.0:
            return '0'
    else:
        return '1'


oxigen = ''
i = 0
lines2 = lines[:]

while (len(lines2) >1):
    most = most_popular(i,lines2)
    tmp =[]
    for l in lines2:
        if l[i] == most:
            tmp.append(l)
    lines2 = tmp[:]
    i = i + 1

oxigen = lines2[0]

i = 0

while (len(lines) >1):
    least = least_popular(i,lines)
    tmp =[]
    for l in lines:
        if l[i] == least:
            tmp.append(l)
    lines = tmp[:]
    i = i + 1

co2 = lines[0]


print oxigen
print co2
print int(co2,2) * int(oxigen, 2)
