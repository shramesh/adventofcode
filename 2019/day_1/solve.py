import math


def calc_fuel_required(mass):
    return math.floor(mass / 3.0) - 2


def fuel_requires_fuel(mass):
    current_fuel = 0
    next_fuel = calc_fuel_required(mass)
    while next_fuel > 0:
        current_fuel += next_fuel
        next_fuel = calc_fuel_required(next_fuel)
    return current_fuel


def part_1():

    i_o_s = [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
    for i, o in i_o_s:
        assert calc_fuel_required(i) == o, f"{calc_fuel_required(i)} is not equal to {o}"

    with open("input.txt", "r") as ip:
        masses = [int(x.strip()) for x in ip.readlines()]
        return sum(map(calc_fuel_required, masses))


def part_2():

    i_o_s = [(14, 2), (1969, 966), (100756, 50346)]
    for i, o in i_o_s:
        assert fuel_requires_fuel(i) == o, f"{fuel_requires_fuel(i)} is not equal to {o}"

    with open("input.txt", "r") as ip:
        masses = [int(x.strip()) for x in ip.readlines()]
        return sum(map(fuel_requires_fuel, masses))


if __name__ == '__main__':
    answer_1 = part_1()
    print(answer_1)
    answer_2 = part_2()
    print(answer_2)
