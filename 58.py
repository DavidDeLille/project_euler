#!/usr/bin/python
# -*- coding: utf8 -*-

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
# (prime spiral image on website)
# It is interesting to note that the odd squares lie along the bottom right diagonal, 
# but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# Idea:
# Iteratively calculate the 4 new diagonal numbers and check if the condition is fulfilled
# sidelength = 1+2*i

import primes

def add_to_lists(x):
	if primes.is_prime(x):
		primes_list.append(x)
	else:
		nonprimes_list.append(x)

i = 1
x = 1
r = 0
primes_list = []
nonprimes_list = [1]

while True:
	for a in range(4):
		x += 2*i
		add_to_lists(x)

	r = len(primes_list)*100/(len(primes_list)+len(nonprimes_list))
	if r < 10:
		print "i:", i
		print "sidelength:",1+2*i
		exit()

	i += 1

# Answer = 26241 (i = 13120)