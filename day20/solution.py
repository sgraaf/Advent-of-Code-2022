from aocli import read, to_lines

print("--- Day 20: Grove Positioning System ---")

# read the input data from `input.txt`
data = list(enumerate(map(int, to_lines(read("input.txt")))))
original_data = tuple(data)


def mix(original_data: tuple[tuple[int, int]], data: list[tuple[int, int]]) -> None:
    for original_i, val in original_data:
        i = data.index((original_i, val))
        data.pop(i)
        data.insert((i + val) % len(data), (original_i, val))


# part one
print("--- Part One ---")
mix(original_data, data)

print(
    sum(
        data[([val for _, val in data].index(0) + n) % len(data)][1]
        for n in (1000, 2000, 3000)
    )
)

# part two
print("--- Part Two ---")
data = [(i, val * 811589153) for i, val in original_data]
original_data = tuple(data)

for round in range(10):
    mix(original_data, data)

print(
    sum(
        data[([val for _, val in data].index(0) + n) % len(data)][1]
        for n in (1000, 2000, 3000)
    )
)
