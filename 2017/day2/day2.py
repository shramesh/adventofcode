# -*- coding: utf-8 -*-
# @Author: shramesh
# @Date:   2017-12-01 23:52:27
# @Last Modified by:   shramesh
# @Last Modified time: 2017-12-02 00:12:05

#Part 2
from itertools import combinations
with open("input.txt") as ip:
	sum = 0
	for line in ip.readlines():
		captcha_digits = [int(x) for x in line.strip().split()]
		pairs = combinations(captcha_digits,2)
		for pair in pairs:
			if (pair[0])%(pair[1]) == 0:
				sum += pair[0]/pair[1]
			elif (pair[1])%(pair[0]) == 0:
				sum += pair[1]/pair[0]
	print sum