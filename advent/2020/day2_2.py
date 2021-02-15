#!usr/local/bin/python
# -*- coding: utf-8 -*-
from collections import Counter

f = open('./input2.txt')

total = 0

for l in f:
	# format  1-3 a:
	# translate to tuple
	(policy, pw) = l.split(":")
        (_range, letter) = policy.split()
	(_min, _max) = _range.split("-")
	print "{0}·{1}·{2}·{3}".format(_min,_max, letter, pw)
	pw = pw.strip()
	c = Counter(pw)
	if c.get(letter) is not None and c.get(letter) >= 1:
		_min = int(_min) -1
		_max = int(_max) -1
		
		if pw[_min] ==letter and pw[_max]!=letter:
			total += 1
			print list(pw)
			print "valid"
		elif pw[_min] !=letter and pw[_max]==letter:
			total += 1
			print list(pw)
			print "valid"
print total
