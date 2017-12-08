# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-08 00:01:43
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-08 00:23:59


def cmp(num1,str,num2):
		if str == ">":
			return num1 > num2
		elif str == ">=":
			return num1 >= num2
		elif str == "<=":
			return num1 <= num2
		elif str == "<":
			return num1 < num2
		elif str == "==":
			return num1 == num2
		elif str == "!=":
			return num1 != num2

from collections import defaultdict

def get_highest(_dict):
	return max(_dict.values())

registers = defaultdict(int)
highest_ever = 0
with open("input.txt") as ip:
	for line in ip.readlines():
		# um inc -671 if lbf != 5
		register_val, action, reg_num, _, cmp_reg, cmp_action, cmp_num = line.strip().split(" ")
		reg_num = int(reg_num)
		cmp_num = int(cmp_num)		
		if action == "inc":
			if cmp(registers[cmp_reg],cmp_action,cmp_num): 
				registers[register_val] += reg_num
		elif action == "dec":
			if cmp(registers[cmp_reg],cmp_action,cmp_num): 
				registers[register_val] -= reg_num
		if get_highest(registers) > highest_ever :
			highest_ever = get_highest(registers)

print sorted(registers.iteritems(), key=lambda (k,v): (v,k), reverse=True)[0]
print highest_ever
