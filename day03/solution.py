from aocli import read, to_lines

print("--- Day 3: Rucksack Reorganization ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))


def get_priority(t: str) -> int:
    if t.isupper():
        return ord(t) - 38
    return ord(t) - 96


# part one
print("--- Part One ---")
priorities = 0
for line in data:
    parts = line[: int(len(line) / 2)], line[int(len(line) / 2) :]
    common_type = set.intersection(*map(set, parts)).pop()
    priorities += get_priority(common_type)
print(priorities)

# part two
print("--- Part Two ---")
priorities = 0
n = 3
for i in range(0, len(data), n):
    lines = data[i : i + n]
    common_type = set.intersection(*map(set, lines)).pop()
    priorities += get_priority(common_type)
print(priorities)
