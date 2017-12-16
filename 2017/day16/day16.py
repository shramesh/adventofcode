# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-16 04:52:36
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-16 06:10:40



def spin(curr_position,x):
	chars = [char for char in curr_position]
	return "".join(chars[-x:]+chars[:len(curr_position)-x])


def exchange(curr_position,A,B):
	chars = [char for char in curr_position]
	temp = chars[A]
	chars[A] = chars[B]
	chars[B] = temp
	return "".join(chars)

def partner(curr_position,A,B):
	chars = [char for char in curr_position]
	A_index = chars.index(A.lower())
	B_index = chars.index(B.lower())
	chars[A_index] = B.lower()
	chars[B_index] = A.lower()
	return "".join(chars)

curr_position = "abcdefghijklmnop"

count = 1000000000
seen = []
while True:
	if curr_position in seen:
		print seen[count%len(seen)]
		break
	seen.append(curr_position)	
	for move in open("input.txt").read().split(","):
		if move.startswith("s"):
			curr_position = spin(curr_position,int(move[1:]))
		elif move.startswith("x"):
			curr_position = exchange(curr_position,int("".join(move[1:move.index("/")])),int("".join(move[move.index("/")+1:])))
		elif move.startswith("p"):
			curr_position = partner(curr_position,"".join(move[1:move.index("/")]),"".join(move[move.index("/")+1:]))

# print curr_position
