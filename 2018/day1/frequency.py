"""
Day 1: Compute frequency starting from zero and after applying the changes in input.txt
"""
import re

sign_value_tuples = []
for sign_value in open("input.txt").readlines():
    m = re.match(r"([+-])(\d+)", sign_value)
    sign = m.group(1)
    value = int(m.group(2))
    sign_value_tuples.append((sign, value))

start_val = 0
round_1_values = []
for i, j in sign_value_tuples:
    if i == "+":
        start_val += j
    else:
        start_val -= j
    round_1_values.append(start_val)

# part 1
print(start_val)

dup_found = False
while not dup_found:
    for i, j in sign_value_tuples:
        if i == "+":
            start_val += j
        else:
            start_val -= j
        if start_val in round_1_values:
            # part 2
            print(start_val)
            dup_found = True
            break