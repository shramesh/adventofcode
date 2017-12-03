# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-03 02:05:04
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-03 05:19:33


def print_grid(matrix):
	for row in matrix:
		print row

def get_grid_dim(num):
	i = 1	 
	while True:
		if num <= i**2:
			grid_dim = i 
			break
		else:
			i += 1
	return grid_dim


def fill_odd_grid(grid,grid_dim,max_grid_col_id,max_grid_row_id):
	max_num = grid_dim**2

	grid[max_grid_row_id][max_grid_col_id] = max_num
	
	row_id = max_grid_row_id
	col_id = max_grid_col_id - 1

	curr_num = max_num - 1
	for col_id in range(col_id,max_grid_col_id-grid_dim,-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 1 - right to left"
		# print_grid(grid)
		# print "******"
	
	row_id-=1	
	for row_id in range(row_id,max_grid_row_id-grid_dim,-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 2 - bottom to top"
		# print_grid(grid)
		# print "******"
	
	col_id += 1
	for col_id in range(col_id,col_id+grid_dim-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 3 - left to right"
		# print_grid(grid)
		# print "******"
	
	row_id+=1	
	for row_id in range(row_id,row_id+grid_dim-2):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 4 - top to bottom"
		# print_grid(grid)
		# print "******"

	return grid,max_grid_col_id-1,max_grid_row_id-1

def fill_even_grid(grid,grid_dim,min_grid_col_id,min_grid_row_id):
	max_num = grid_dim ** 2

	grid[min_grid_row_id][min_grid_col_id] = max_num
	row_id = min_grid_row_id
	col_id = min_grid_col_id + 1
	curr_num = max_num - 1

	for col_id in range(col_id,col_id+grid_dim-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 1 - left to right"
		# print_grid(grid)
		# print "******"

	row_id+=1	
	for row_id in range(row_id,row_id+grid_dim-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 2 - top to bottom"
		# print_grid(grid)
		# print "******"

	col_id-=1 
	for col_id in range(col_id,min_grid_col_id-1,-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 3 - right to left"
		# print_grid(grid)
		# print "******"
	row_id-=1	
	for row_id in range(row_id,min_grid_row_id,-1):
		grid[row_id][col_id] = curr_num
		curr_num -= 1
		# print "Loop 4 - bottom to top"
		# print_grid(grid)
		# print "******"

	return grid,min_grid_col_id+1,min_grid_row_id+1

def get_grid(num):
	grid_dim = get_grid_dim(num)
	grid = []
	for i in range(grid_dim):
		grid.append([0]*grid_dim)
	max_num = grid_dim ** 2	
	if grid_dim % 2 == 0: #top-left has the max num
		min_col_id = 0
		min_row_id = 0
		for gd in range(grid_dim,0,-2):
			grid,min_col_id,min_row_id = fill_even_grid(grid,gd,min_col_id,min_row_id)
	else:
		max_col_id = grid_dim-1
		max_row_id = grid_dim-1
		for gd in range(grid_dim,-1,-2):
			grid,max_col_id,max_row_id = fill_odd_grid(grid,gd,max_col_id,max_row_id)
	print_grid(grid)
	return grid

def get_index_of(num,grid):
	for idx,row in enumerate(grid):
		if num in row:
			return idx,row.index(num)

def find_manhattan_distance(num):
	grid = get_grid(num)
	x_1,y_1 = get_index_of(1,grid)
	x_num,y_num = get_index_of(num,grid)
	return abs(x_num-x_1)+abs(y_num-y_1)
	
import sys
print find_manhattan_distance(int(sys.argv[1]))