import re
from collections import defaultdict
from copy import deepcopy

from aocli import read, to_lines

print("--- Day 5: Supply Stacks ---")

# read the input data from `input.txt`
puzzle = read("input.txt").split("\n\n")

data = defaultdict(list)
for line in reversed(to_lines(puzzle[0])):
    for crate_match in re.finditer(r"\[([A-Z])\]", line):
        data[crate_match.start() // 4 + 1].append(crate_match.group(1))
_data = deepcopy(data)

rearrangements = []
for line in to_lines(puzzle[1]):
    rearrangements.append(tuple(map(int, re.findall(r"\d+", line))))

# part one
print("--- Part One ---")
for n, src, dest in rearrangements:
    for _ in range(n):
        data[dest].append(data[src].pop())

print("".join(data[x][-1] for x in sorted(data.keys())))

# part two
print("--- Part Two ---")
data = _data
for n, src, dest in rearrangements:
    data[dest] += data[src][-n:]
    data[src] = data[src][:-n]

print("".join(data[x][-1] for x in sorted(data.keys())))
