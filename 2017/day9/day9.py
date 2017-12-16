# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-15 19:35:33
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-15 21:10:43


def clean_up_garbage(input):
	clean_input = []
	skip_indices = []
	no_of_garbage_chars = 0
	for index,char in enumerate(input):
		if index in skip_indices:
			continue
		if char == "<":
			j = index + 1
			while(True):
				if input[j] == "!":
					skip_indices.append(j) 
					skip_indices.append(j+1)
					j += 2
				elif input[j] == ">":
					skip_indices.append(j)	
					break
				else:
					no_of_garbage_chars += 1
					skip_indices.append(j)	
					j += 1
		elif char == "!":
			skip_indices.append(j+1)
		else:
			clean_input.append(char)

	return "".join(clean_input), no_of_garbage_chars


def get_score(input):
	paren_stack = []
	no_of_open_parens = 0
	score = 0
	for index, char in enumerate(input):
		print char,paren_stack,score
		if char == "{":
			paren_stack.append(char)
			no_of_open_parens += 1
		elif char == "}":
			assert paren_stack[len(paren_stack)-1] == "{", "Not matching"
			del paren_stack[len(paren_stack)-1]
			score += no_of_open_parens
			no_of_open_parens -= 1
		else:
			continue
	return score

input = open("input.txt").read()
clean_input,num_garbage_chars = clean_up_garbage(input)
# clean_input = clean_up_garbage("{{<a!>},{<a!>},{<a!>},{<ab>}}")

print clean_input
print get_score(clean_input)
print num_garbage_chars
# def find_groups(input):
