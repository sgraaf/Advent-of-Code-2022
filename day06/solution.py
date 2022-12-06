from aocli import read

print("--- Day 6: Tuning Trouble ---")

# read the input data from `input.txt`
data = read("input.txt").strip()


def find_marker(data: str, n: int) -> int:
    for i in range(len(data) - n + 1):
        if len(set(data[i : i + n])) == n:
            return i + n
    return -1


# part one
print("--- Part One ---")
print(find_marker(data, 4))

# part two
print("--- Part Two ---")
print(find_marker(data, 14))
