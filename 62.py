#!/usr/bin/python
# -*- coding: utf8 -*-

# The cube, 41063625 (345³), can be permuted to produce two other cubes: 56623104 (384³) and 66430125 (405³).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.

# Idea:
# Loop all integers, and transform the cube into a string that characterizes that cube (digits aranged numerically). 
# Store those strings into dictionary of lists. Program ends when one of the dictionary lists has 5 elements.


my_dict = dict()
i = 1
max = 0

while True:
	string = ''.join(sorted(str(pow(i,3))))
	#print string

	l = my_dict.setdefault(string, list())
	l.append(i)
	my_dict[string] = l
	x = len(l)

	if x > max:
		print "new max: %d"%x
		print l
		print
		max = x

	i+=1

	if x == 5:
		answer = pow(l[0],3)
		print "Answer: %d"%answer
		exit()

# Answer = 127035954683