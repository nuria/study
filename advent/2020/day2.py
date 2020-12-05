#!usr/local/bin/python
# -*- coding: utf-8 -*-
from collections import Counter

f = open('./input2.txt')

total = 0

for l in f:
	total = total + 1
	# format  1-3 a:
	# translate to tuple
	(policy, pw) = l.split(":")
        (_range, letter) = policy.split()
	(_min, _max) = _range.split("-")
	c = Counter(pw)
	#print·"{0}·{1}·{2}·{3}".format(_min,_max,·letter,··pw)

	if c.get(letter) is None:
		total = total -1
	elif c[letter] > int(_max) or c[letter] < int(_min):
		total = total -1

print total
