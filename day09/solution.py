import re

from aocli import read, to_lines

print("--- Day 9: Rope Bridge ---")

# read the input data from `input.txt`
data = []
for line in to_lines(read("input.txt")):
    if m := re.match(r"([UDLR]) (\d+)", line):
        data.append((m.group(1), int(m.group(2))))


def update_head(x_head: int, y_head: int, direction: str) -> tuple[int, int]:
    if direction == "U":
        y_head += 1
    elif direction == "D":
        y_head -= 1
    elif direction == "L":
        x_head -= 1
    elif direction == "R":
        x_head += 1
    return x_head, y_head


def update_tail(x_head: int, y_head: int, x_tail: int, y_tail: int) -> tuple[int, int]:
    if abs(x_head - x_tail) > 1 or abs(y_head - y_tail) > 1:
        if x_head > x_tail:
            x_tail += 1
        elif x_head < x_tail:
            x_tail -= 1
        if y_head > y_tail:
            y_tail += 1
        elif y_head < y_tail:
            y_tail -= 1
    return x_tail, y_tail


# part one
print("--- Part One ---")
# naive approach
x_head, y_head = x_tail, y_tail = 0, 0
visited = set()
visited.add((x_tail, y_tail))
for direction, amount in data:
    for _ in range(amount):
        # update the head
        x_head, y_head = update_head(x_head, y_head, direction)

        # check and update the tail
        x_tail, y_tail = update_tail(x_head, y_head, x_tail, y_tail)

        # add the tail to the visited set
        visited.add((x_tail, y_tail))

print(len(visited))

# part two
print("--- Part Two ---")
# smart approach
x_start, y_start = 0, 0
visiteds = {}
for i in range(10):
    visiteds[i] = [(x_start, x_start)]

for direction, amount in data:
    for _ in range(amount):
        for knot, visited in visiteds.items():
            x, y = visited[-1]
            if not knot:  # head
                x, y = update_head(x, y, direction)
            else:  # tail
                x_head, y_head = visiteds[knot - 1][-1]
                x, y = update_tail(x_head, y_head, x, y)

            visited.append((x, y))

print(len(set(visiteds[9])))
