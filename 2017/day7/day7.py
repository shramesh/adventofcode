# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-07 00:07:17
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-07 00:27:44


parents_of_x = {}
children_of_x = {}
weights = {}
with open("input.txt") as ip:
	for line in ip.readlines():
		if "->" in line:
			left_children, right_children = line.split("->")
			children_of_x[left_children.split(" ")[0]] = []
			for rc in right_children.strip().split(","):
				parents_of_x[rc.strip()] = left_children.split(" ")[0]
				children_of_x[left_children.split(" ")[0]].append(rc.strip())  
			weights[left_children.split(" ")[0]] = int(left_children.split(" ")[1].strip().replace("(","").replace(")",""))

# print parents_of_x

random = parents_of_x.keys()[0]
bottom = None
while True:
	try:
		random = parents_of_x[random]
	except KeyError:
		bottom = random
		break



print bottom