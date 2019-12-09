import tqdm
INPUT_RANGE = (273025, 767253)


def check_valid_password(number):
    def six_digit(x):
        # print(x, "six digit", len(str(x)) == 6)
        return len(str(x)) == 6

    def within_range(x):
        # print(x, "within range", INPUT_RANGE[0] <= x <= INPUT_RANGE[1])
        return INPUT_RANGE[0] <= x <= INPUT_RANGE[1]

    def atleast_two_adj_same(x):
        for i, j in zip(str(x)[:-1], str(x)[1:]):
            if i == j:
                # print("adj same", True)
                return True
        # print("adj same", False)
        return False

    def atleast_two_adj_same_not_part_of_bigger_group(x):
        # TODO: replace this with a method using regex for capturing repeating digit patterns
        for char_index, (i, j) in enumerate(zip(str(x)[:-1], str(x)[1:])):
            if i == j:
                # last char of string
                if char_index + 2 > len(str(x)) - 1:
                    if str(x)[char_index - 1] != j:
                        return True
                else:
                    if str(x)[char_index + 2] != j:
                        # first char
                        if char_index - 1 < 0:
                            return True
                        else:
                            if str(x)[char_index - 1] !=j:
                                return True
        return False

    def monotonically_increasing(x):
        for i, j in zip(str(x)[:-1], str(x)[1:]):
            if j < i:
                # print("mono increasing", False)
                return False
        # print("mono increasing", True)
        return True

    # part 1
    # return all(func(number) for func in [six_digit, within_range, atleast_two_adj_same, monotonically_increasing])

    # part 2
    return all(func(number) for func in [six_digit, within_range, atleast_two_adj_same_not_part_of_bigger_group,
                                         monotonically_increasing])


# part 1
i_o_s = [(111111, True),
         (223450, False),
         (123789, False)]

# for i, o in i_o_s:
#     assert check_valid_password(i) == o,\
#         f"{i}->{check_valid_password(i)} is not equal to {o} : ensure within range check is disabled for these assertions"
#     print(f"Test case {i}->{o} passed!")

# part 2
i_o_s = [(112233, True),
         (123444, False),
         (111122, True)]
# ensure within range check is disabled for these assertions
for i, o in i_o_s:
    assert check_valid_password(i) == o,\
        f"{i}->{check_valid_password(i)} is not equal to {o}"
    print(f"Test case {i}->{o} passed!")

valid_nums = []

for num in tqdm.trange(INPUT_RANGE[0], INPUT_RANGE[1] + 1):
    if check_valid_password(num):
        valid_nums.append(num)

print(len(valid_nums))