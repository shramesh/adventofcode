# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-04 04:44:26
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-04 04:53:37


from itertools import combinations

def is_valid(line):
	words = line.strip().split()
	return len(set(words)) == len(words)

def is_anagram(w1,w2):
	if len(w1) == len(w2):
		for c1 in w1:
			if c1 not in w2:
				return False
		for c2 in w2:
			if c2 not in w1:
				return False
		return True
	else:
		return False		

def is_anagram_valid(line):
	words = line.strip().split()
	valid=True
	for w1,w2 in combinations(words,2):
		if is_anagram(w1,w2):
			valid = False
			break
	return valid

novalid = 0
with open("input.txt") as ip:
	for line in ip.readlines():
		if is_anagram_valid(line):
			novalid+=1
print novalid

