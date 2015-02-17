#!/usr/bin/python
# -*- coding: utf8 -*-

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

# Explanation:
# xb = 1+1/(1+xa)
# xb = tb/nb, xa = ta/na
# ==> tb = na*2+ta ; nb = na+ta
# if x1 = 1+1/2, then x0 = 1 (or also: t0=1 and n0=1)

import math

ta = 1 	# numerator
na = 1 	# denumerator
count = 0

for i in range(1000):
	tb = na*2+ta
	nb = na+ta

	digits_ta = math.floor(math.log(ta, 10))
	digits_na = math.floor(math.log(na, 10))

	if digits_ta > digits_na:
		count +=1

	ta = tb
	na = nb

print "Answer:", count
# Answer = 153