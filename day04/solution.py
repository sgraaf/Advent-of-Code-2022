import re

from aocli import read, to_lines

print("--- Day 4: Camp Cleanup ---")


def extract_assignments(s: str) -> tuple[int, int]:
    start, end = tuple(map(int, re.match(r"(\d+)-(\d+)", s).groups()))
    return set(range(start, end + 1))


# read the input data from `input.txt`
data = []
for line in to_lines(read("input.txt")):
    parts = line.split(",")
    data.append(tuple(map(extract_assignments, parts)))

# part one
print("--- Part One ---")
count = 0
for assignment_1, assignment_2 in data:
    if assignment_1 <= assignment_2 or assignment_2 <= assignment_1:
        count += 1

print(count)

# part two
print("--- Part Two ---")
count = 0
for assignments in data:
    if set.intersection(*assignments):
        count += 1

print(count)
