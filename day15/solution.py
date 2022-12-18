import re
from itertools import product

from aocli import read, to_lines

print("--- Day 15: Beacon Exclusion Zone ---")

# read the input data from `input.txt`
data = {}
for line in to_lines(read("input.txt")):
    x_sensor, y_sensor, x_beacon, y_beacon = map(int, re.findall(r"(\-?\d+)", line))
    data[(x_sensor, y_sensor)] = (x_beacon, y_beacon)


def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


# part one
print("--- Part One ---")
row = 2_000_000
blocked = set()
for (x_sensor, y_sensor), (x_beacon, y_beacon) in data.items():
    beacon_distance = manhattan(x_sensor, y_sensor, x_beacon, y_beacon)
    row_distance = abs(y_sensor - row)
    if row_distance <= beacon_distance:
        for x in range(
            x_sensor - (beacon_distance - row_distance),
            x_sensor + (beacon_distance - row_distance) + 1,
        ):
            if (x, row) in {(x_sensor, y_sensor), (x_beacon, y_beacon)}:
                continue
            blocked.add(x)

print(len(blocked))

# part two
print("--- Part Two ---")
distances = {
    (x_sensor, y_sensor): manhattan(x_sensor, y_sensor, x_beacon, y_beacon)
    for (x_sensor, y_sensor), (x_beacon, y_beacon) in data.items()
}

# get coefficients (a) for boundaries of the scanner range of the form y = x + a
pos_as, neg_as = [], []
for ((x, y), distance) in distances.items():
    pos_as.append(y - x + distance + 1)
    pos_as.append(y - x - distance - 1)
    neg_as.append(x + y + distance + 1)
    neg_as.append(x + y - distance - 1)
pos_as = {a for a in pos_as if pos_as.count(a) >= 2}
neg_as = {b for b in neg_as if neg_as.count(b) >= 2}

bound = 4_000_000
for pos_a, neg_a in product(pos_as, neg_as):
    x_p, y_p = (neg_a - pos_a) // 2, (pos_a + neg_a) // 2
    if 0 < x_p < bound and 0 < y_p < bound:
        if all(
            manhattan(x_p, y_p, x_sensor, y_sensor) > distance
            for (x_sensor, y_sensor), distance in distances.items()
        ):
            print(4_000_000 * x_p + y_p)
