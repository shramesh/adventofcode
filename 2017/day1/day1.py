# -*- coding: utf-8 -*-
# @Author: harsha
# @Date:   2017-12-01 00:24:01
# @Last Modified by:   harsha
# @Last Modified time: 2017-12-01 00:39:01


#Part 1
with open("input.txt") as ip:
	for line in ip.readlines():
		captcha_digits = [int(x) for x in line.strip()]
		part1_sum = 0
		part2_sum = 0
		for idx,digit in enumerate(captcha_digits):
			if digit == captcha_digits[(idx+1)%len(captcha_digits)]:
				part1_sum+=digit
			if digit == captcha_digits[(idx+len(captcha_digits)/2)%len(captcha_digits)]:
				part2_sum+=digit
		print "part1_sum:{}".format(part1_sum)
		print "part2_sum:{}".format(part2_sum)