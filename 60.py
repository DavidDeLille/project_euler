#!/usr/bin/python
# -*- coding: utf8 -*-

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# Idea:

import primes
import bisect

def check_list(l, x):
	"""Are all concatenations of the elements of the given list with the given number prime?"""
	if len(l) == 0:
		return True

	y = str(l[0])
	if not primes.is_prime(int(str(x)+y), primes_list):
		return False
	if not primes.is_prime(int(y+str(x)), primes_list):
		return False
	return check_list(l[1:], x)

prime = 2
primes_list = list()
list2 = list()
list3 = list()
list4 = list()

while True:
	prime = primes.get_next_prime(prime, primes_list)
	index = bisect.bisect_left(primes_list, prime)

	# update list2
	for p in primes_list[:index]:
		if check_list([p], prime):
			list2.append([p, prime])

	# update list3
	for l in list2:
		if check_list(l, prime):
			list3.append(l+[prime])

	# update list4
	for l in list3:
		if check_list(l, prime):
			list4.append(l+[prime])

	# check if any list5
	for l in list4:
		if check_list(l, prime):
			print l+[prime]
			print "Answer:", sum(l+[prime])
			exit()

# [13, 5197, 5701, 6733, 8389]
# Answer: 26033

