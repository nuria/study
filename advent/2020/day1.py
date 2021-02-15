#!usr/local/bin/python

f = open ('./input1.txt')

data = {}
for l in f:
	target = 2020 -int(l)
	data[int(l)] = target

# now figure out the entries that sum up to 2020
complementary = {}


for k in data.keys():
	target = data[k]
	if data.get(target) is not None:
		print  k * target
		break
 


