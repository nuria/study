#!usr/local/bin

f = open('./input15.txt')

items = []
reverse = {}

turn = 1

for l in f:
	item = int(l.strip())
	items.append(item)
	if reverse.get(item) is None:
		reverse[item] = []
	l = reverse[item]
	l.append(turn)
	turn += 1 

limit = 30000001

current = items[-1]

while  turn < limit:
	last = current
	if len(reverse[last]) == 1:
		reverse[0].append(turn)
		current = 0
	else:
		# check age 
		age = reverse[last][-1] - reverse[last][-2]
		items.append(age)
		if reverse.get(age) is None:
			reverse[age] = []
		reverse[age].append(turn)
		current = age	
	turn += 1

	#print reverse

print current 
	
