# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-04 23:53:08
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-05 00:34:52


with open("input.txt") as ip:
	maze = [int(x.strip()) for x in ip.readlines()]
	# print maze
	current_pointer = 0
	no_steps = 0
	while current_pointer < len(maze):
		# print "cp:{},val:{}".format(current_pointer,maze[current_pointer])
		
		old_offset = maze[current_pointer]
		if maze[current_pointer] >=3:
			maze[current_pointer]-=1
		else:
			maze[current_pointer]+=1
		
		current_pointer += old_offset
		no_steps += 1
		
	print no_steps