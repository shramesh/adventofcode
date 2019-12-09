import random
from copy import copy


def eval_intcode(numbers, all_nums):
    if len(numbers) != 4 and numbers[0] == 99:
        return 0
    opcode = numbers[0]
    pos_ip_1 = numbers[1]
    ip_1 = get_num_at_position(pos_ip_1, all_nums)

    pos_ip_2 = numbers[2]
    ip_2 = get_num_at_position(pos_ip_2, all_nums)

    pos_op_1 = numbers[3]
    if opcode == 1:
        all_nums[pos_op_1] =ip_1 + ip_2
        return 1
    elif opcode == 2:
        all_nums[pos_op_1] = ip_1 * ip_2
        return 1
    else:
        return 0


def get_num_at_position(position, all_nums):
    return all_nums[position]


def get_next_intcode(curr_index, all_nums):
    next_index = curr_index + 4
    return next_index, all_nums[next_index:next_index+4]


def process_nums(all_nums):
    curr_index = 0
    intcode = all_nums[curr_index: curr_index + 4]
    while 1:
        output = eval_intcode(intcode, all_nums)
        if not output:
            break
        else:
            curr_index, intcode = get_next_intcode(curr_index, all_nums)
    return all_nums


i_o_s = [([1,0,0,0,99], [2,0,0,0,99]),
         ([2,3,0,3,99], [2,3,0,6,99]),
         ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
         ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])]

for i, o in i_o_s:
    assert process_nums(i) == o, f"{process_nums(i)} is not equal to {o}"
    print(f"Test case {i}->{o} passed!")


def eval_and_find_at_address(noun, verb, all_nums):
    all_nums[1] = noun
    all_nums[2] = verb
    all_nums = process_nums(all_nums)
    return all_nums



def identify_noun_verb_combination(all_nums):
    all_choices = range(0, len(all_nums))
    picked_choices = []

    while 1:
        noun, verb = random.choice(all_choices), random.choice(all_choices)
        if (noun, verb) in picked_choices:
            continue
        else:
            picked_choices.append((noun, verb))
        run_nums_copy = copy(all_nums)
        run_nums_copy = eval_and_find_at_address(noun, verb, run_nums_copy)
        output = run_nums_copy[0]
        print(f"Found {output}")
        if output == 19690720:
            print(f"Noun:{noun} Verb:{verb} is the solution!")
            break



with open("input.txt") as ip:
    all_nums = list(map(int, ip.read().split(",")))
    # all_nums[1] = 12
    # all_nums[2] = 2
    # all_nums = process_nums(all_nums)
    # print(all_nums)
    # print(all_nums[0])
    identify_noun_verb_combination(all_nums)
