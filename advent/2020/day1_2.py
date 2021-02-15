#!usr/local/bin/python

f = open ('./input1.txt')

data = {}
for l in f:
	target = 2020 -int(l)
	data[int(l)] = target

# now figure out the entries that sum up to 2020
complementary = {}

items = data.keys()

for i in range(0, len(items)):
	for 	j in range(i+1, len(items)):
		target = 2020 - items[i] - items[j]

		if data.get(target) is not None:
			print  target * items[i] * items[j]
			break
 


