#!/usr/bin/python
# -*- coding: utf8 -*-

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

# Idea: Loop formats (e.g. 54*2). 
# For each format, determine how many primes it can generate. 
# Keep creating more formats until an 8-prime format is found.

import primes

def count_primes(f):
	"""Determine how many primes can be created using this format."""
	ret_list = []
	for c in "0123456789":
		temp = f.replace('*', c)
		if primes.is_prime(int(temp), primes_list) and temp[0] != '0':
			ret_list.append(temp)
	return ret_list

digits = "0123456789*"
word_list = [""]
primes_list = [] # list to store prime numbers (so they have to be calculated several times)
my_max = 0

while True: # each loop increases the length of the word list
	word_list = [a+b for a in word_list for b in digits] 	# take every word and append every digit; this will create a list of all words of a certain length
	format_list = [w for w in word_list if '*' in w]		# we only need to test the words that contain a '*'

	print "word length:", len(word_list[0])

	for f in format_list:
		temp_list = count_primes(f)
		count = len(temp_list)
		
		if count > my_max:
			print "new max: %d"%count
			my_max = count
			print f
			print temp_list
			print
		
		if count == 8:
			exit()

# Answer = 121313 (format = "*2*3*3")