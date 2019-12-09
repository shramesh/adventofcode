from collections import defaultdict

def get_all_coordinates(wire):
    curr_pos = [0, 0]
    wire_coordinates = set()
    wire_coordinates.add(tuple(curr_pos))
    for move in wire.split(","):
        dir = move[0]
        num_moves = int(move[1:])
        if dir == "R":
            for i in range(num_moves):
                curr_pos[0] += 1
                wire_coordinates.add(tuple(curr_pos))
        elif dir == "L":
            for i in range(num_moves):
                curr_pos[0] -= 1
                wire_coordinates.add(tuple(curr_pos))
        elif dir == "U":
            for i in range(num_moves):
                curr_pos[1] += 1
                wire_coordinates.add(tuple(curr_pos))
        elif dir == "D":
            for i in range(num_moves):
                curr_pos[1] -= 1
                wire_coordinates.add(tuple(curr_pos))
    return wire_coordinates


def get_steps_to_a_point_on_a_wire(point, wire):
    # print(f"finding distance to a {point} on the {wire}")
    curr_pos = [0, 0]
    steps_to_reach_different_points = defaultdict(int)
    steps_to_reach_different_points[tuple(curr_pos)] = 0
    for move in wire.split(","):

        dir = move[0]
        num_moves = int(move[1:])

        if dir == "R":
            for i in range(num_moves):
                prev_pos = curr_pos[:]
                curr_pos[0] += 1
                steps_to_reach_different_points[tuple(curr_pos)] = steps_to_reach_different_points[tuple(prev_pos)] + 1
                if curr_pos == list(point):
                    return steps_to_reach_different_points[tuple(curr_pos)]

        elif dir == "L":
            for i in range(num_moves):
                prev_pos = curr_pos[:]
                curr_pos[0] -= 1
                steps_to_reach_different_points[tuple(curr_pos)] = steps_to_reach_different_points[tuple(prev_pos)] + 1
                if curr_pos == list(point):
                    return steps_to_reach_different_points[tuple(curr_pos)]

        elif dir == "U":
            for i in range(num_moves):
                prev_pos = curr_pos[:]
                curr_pos[1] += 1
                steps_to_reach_different_points[tuple(curr_pos)] = steps_to_reach_different_points[tuple(prev_pos)] + 1
                if curr_pos == list(point):
                    return steps_to_reach_different_points[tuple(curr_pos)]

        elif dir == "D":
            for i in range(num_moves):
                prev_pos = curr_pos[:]
                curr_pos[1] -= 1
                steps_to_reach_different_points[tuple(curr_pos)] = steps_to_reach_different_points[tuple(prev_pos)] + 1
                if curr_pos == list(point):
                    return steps_to_reach_different_points[tuple(curr_pos)]


def get_best_intersection_point(wires, min_dist_or_steps):
    all_wire_coordinates = []
    for wire in wires:
        all_wire_coordinates.append(get_all_coordinates(wire))
    intersecting_points = set.intersection(*all_wire_coordinates)
    if min_dist_or_steps == "dist":
        min_distance = min([abs(i[0]) + abs(i[1]) for i in intersecting_points if i != (0, 0)])
        return min_distance
    else:
        all_total_steps = []
        for i in intersecting_points:
            if i == (0, 0):
                continue
            total_steps = 0
            for w in wires:
                print(i)
                total_steps += get_steps_to_a_point_on_a_wire(i, w)
            print("\n\n")
            all_total_steps.append(total_steps)
        print(all_total_steps)
        return min(all_total_steps)


i_o_s = [(["R8,U5,L5,D3", "U7,R6,D4,L4"], 6),
         (["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], 159),
         (["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 135)]

for i, o in i_o_s:
    # print(get_intersecting_points(i))
    assert get_best_intersection_point(i, min_dist_or_steps="dist") == o,\
        f"{get_best_intersection_point(i, min_dist_or_steps='dist')} is not equal to {o}"
    print(f"Test case {i}->{o} passed!")


i_o_s = [(["R8,U5,L5,D3", "U7,R6,D4,L4"], 30),
         (["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], 610),
         (["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 410)]

for i, o in i_o_s:
    # print(get_intersecting_points(i))
    assert get_best_intersection_point(i, min_dist_or_steps="steps") == o,\
        f"{get_best_intersection_point(i, min_dist_or_steps='steps')} is not equal to {o}"
    print(f"Test case {i}->{o} passed!")


with open("input.txt") as ip:
    wires = [wire.strip() for wire in ip.readlines() if wire.strip()]
    # print(wires)
    # print(get_best_intersection_point(wires, min_dist_or_steps="dist"))
    print(get_best_intersection_point(wires, min_dist_or_steps="steps"))
