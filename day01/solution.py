from aocli import read, to_numbers

print("--- Day 1: Calorie Counting ---")

# read the input data from `input.txt`
data = list(map(to_numbers, read("input.txt").split("\n\n")))

# part one
print("--- Part One ---")
print(max(sum(calories) for calories in data))

# part two
print("--- Part Two ---")
print(sum(sorted(sum(calories) for calories in data)[-3:]))
