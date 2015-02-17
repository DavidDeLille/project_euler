#!/usr/bin/python
# -*- coding: utf8 -*-

# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
# - High Card: Highest value card.
# - One Pair: Two cards of the same value.
# - Two Pairs: Two different pairs.
# - Three of a Kind: Three cards of the same value.
# - Straight: All cards are consecutive values.
# - Flush: All cards of the same suit.
# - Full House: Three of a kind and a pair.
# - Four of a Kind: Four cards of the same value.
# - Straight Flush: All cards are consecutive values of same suit.
# - Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). 
# But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.
# (website contains extra example)
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?

# The idea:
# If we get 2 hands, we can assign a absolute score for each hand, and compare the resulting numbers.
# The score I devised consists of 15 digits (the leading ones can be zero).
# The first digit represents the class of the hand (flush, 4-of-a-kind, etc.). This is because the class is the most important aspect of the hand.
# The next 4 digits represent some more detail about the class. These are only used for pairs, triples and full houses. The first 2 show the highest pair/triple and the last 2 show the lowest pair.
# The final 10 digits represent the values of the cards (in descending order). This is used to compare 2 hands in the same class.

# Example 1: 5H 5C 6S 7S KD (Pair of Fives) ==> 100051307060505
# The leading 1 indicates that the class is a pair
# 00 05, shows that there is only 1 pair, and that it is a pair of fives (note that high cards can't be used to compare which pair/double_pair/triple/full house is better)
# 13 07 06 05 05 are the values of the cards; this shows there is a queen, a seven, a six, and 2 fives

# Example 1: 3D 6D 7D TD QD (Flush with Diamonds) ==> 400001210070603
# The leading 4 indicates that the class is a flush
# The next 4 digits are 00 00, because only high cards are looked at in the case of comparing flushes, so there is no need for extra information
# 13 07 06 05 05 are the values of the cards; this shows there is a queen, a seven, a six, and 2 fives

def flush(h):
	"""Is the hand a flush?"""
	suit = h[0][1]
	for c in h[1:]:
		if suit != c[1]:
			return False
	return True

def straight(h):
	"""Is the hand a straight?"""
	values = sorted([card_to_score(c) for c in h])
	for i in range(1, len(values)):
		if values[i] != values[i-1]+1:
			return False
	return True

def score(h):
	"""Calculate the score corresponding to the hand."""
	score = class_score(h)
	values = sorted([card_to_score(c) for c in h], reverse=True)
	for v in values:
		score = score*100 + v
	return score

def class_score(h):
	"""Calculate the (partial) score corresponding to the class of the hand."""
	if flush(h):
		if straight(h):
			return 70000			# straight flush
		else:
			return 40000			# flush
	if straight(h):
		return 30000				# straight
	
	count_dict = count_cards(h)
	if 4 in count_dict.values():
		return 60000				# 4 of a kind
	if 3 in count_dict.values():
		if 2 in count_dict.values():
			temp = card_to_score(find_key(count_dict, 3)[0])
			temp = temp*100 + card_to_score(find_key(count_dict, 2)[0])
			return 50000 + temp		# full house
		else:
			temp = card_to_score(find_key(count_dict, 3)[0])
			return 20000 + temp		# triple
	if 2 in count_dict.values():
		temp = 0
		for c in find_key(count_dict, 2):
			temp = temp*100 + card_to_score(c)
		return 10000 + temp			# pair
	return 0						# high card

def find_key(my_dict, value):
	return sorted([k for k in my_dict if my_dict[k]==value], reverse=True)

def count_cards(h):
	"""Count how often each type of card is present (return a dictionary)."""
	my_dict = dict()
	for c in h:
		value = c[0]
		temp = my_dict.setdefault(value, 0)
		my_dict[value] = temp+1
	return my_dict

def card_to_score(c):
	"""Return the value of the given card."""
	return 2 + "23456789TJQKA".index(c[0])

# # Example from website:
# lines = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD", "5D 8C 9S JS AC 2C 5C 7D 8S QH", "2D 9C AS AH AC 3D 6D 7D TD QD", "4D 6S 9H QH QC 3D 6D 7H QD QS", "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"]

with open("54_poker.txt", 'r') as f:
	lines = f.read().split('\n')[:-1]

count = 0
for l in lines:
	cards = l.split(' ')
	p1 = cards[:5]
	p2 = cards[5:]
	s1 = score(p1)
	s2 = score(p2)

	if s1>s2:
		count += 1

print "Answer:", count
