import re
from copy import deepcopy
from itertools import count

from aocli import read, to_lines

print("--- Day 14: Regolith Reservoir ---")

# read the input data from `input.txt`
data = set()
for line in to_lines(read("input.txt")):
    line_data = []
    for x, y in re.findall(r"(\d+),(\d+)", line):
        line_data.append((int(x), int(y)))

    # extend
    for i, (x_2, y_2) in enumerate(line_data[1:]):
        data.add((x_2, y_2))
        x_1, y_1 = line_data[i]
        if x_1 == x_2:
            for y in range(y_1, y_2, 1 if y_1 < y_2 else -1):
                data.add((x_1, y))
        elif y_1 == y_2:
            for x in range(x_1, x_2, 1 if x_1 < x_2 else -1):
                data.add((x, y_1))
_data = deepcopy(data)

# part one
print("--- Part One ---")
max_y = max(data, key=lambda x: x[1])[1]


def settles(
    data: set[tuple[int, int]], x_sand: int, y_sand: int, y_floor: int = -1
) -> bool:
    x, y = x_sand, y_sand
    while (x, y) not in data:
        new_x, new_y = x, y

        if y_floor <= 0 and y >= max_y:  # check for overflow
            return False

        if new_y + 1 == y_floor:  # check for floor
            break

        if (new_x, new_y + 1) not in data:  # try to move down
            y = new_y + 1
        elif (new_x - 1, new_y + 1) not in data:  # try to move left
            x = new_x - 1
            y = new_y + 1
        elif (new_x + 1, new_y + 1) not in data:  # try to move right
            x = new_x + 1
            y = new_y + 1
        else:
            break

    data.add((x, y))
    return True


x_sand, y_sand = 500, 0
for sand_count in count(1):
    is_settled = settles(data, x_sand, y_sand)
    if not is_settled:
        break

print(sand_count - 1)

# part two
print("--- Part Two ---")
data = _data

for sand_count in count(1):
    is_settled = settles(data, x_sand, y_sand, max_y + 2)
    if (x_sand, y_sand) in data:
        break

print(sand_count)
