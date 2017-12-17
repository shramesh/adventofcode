# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-17 00:18:02
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-17 01:06:36


def spinlock(step_size,no_iters):
	buffer = [0]
	num_to_insert = 1
	curr_pos = 0
	for i in xrange(no_iters):
		pos_to_insert = (step_size + curr_pos) %len(buffer)
		buffer.insert(pos_to_insert+1,num_to_insert)
		curr_pos = pos_to_insert+1		
		num_to_insert += 1
	
	return buffer[curr_pos+1]

assert spinlock(3,2017) == 638

assert spinlock(349,2017) == 640


def spinlock_part2(step_size,no_iters):
	num_after_zero = 0
	curr_pos = 0
	buffer_length = 1
	num_to_insert = 1
	for i in xrange(no_iters):
		pos_to_insert = (step_size + curr_pos) % buffer_length
		if (step_size + curr_pos) % buffer_length == 0:
			num_after_zero = num_to_insert
		buffer_length+=1
		curr_pos = pos_to_insert+1		
		num_to_insert += 1 
	return num_after_zero
# import time
# start = time.time()
# iters = 1000000
# buffer = spinlock(349,iters)
# print buffer[buffer.index(0)+1]
# end = time.time()
# print "Completed {} iters in {} secs".format(iters,end-start)

# print spinlock_part2(3,15)
assert spinlock_part2(3,2017) == 1226 
print spinlock_part2(349,50000000)