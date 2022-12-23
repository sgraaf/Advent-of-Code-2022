from collections import deque
from itertools import product

from aocli import find_neighbouring_indices_3d, read, to_lines

print("--- Day 18: Boiling Boulders ---")

# read the input data from `input.txt`
data = set()
for line in to_lines(read("input.txt")):
    data.add(tuple(map(int, line.split(","))))

# part one
print("--- Part One ---")
sides_count = 0
for i, j, k in data:
    sides_count += 6 - len(data & set(find_neighbouring_indices_3d(i, j, k)))

print(sides_count)

# part two
print("--- Part Two ---")

min_i, max_i, min_j, max_j, min_k, max_k = (
    min(i for i, j, k in data) - 1,
    max(i for i, j, k in data) + 1,
    min(j for i, j, k in data) - 1,
    max(j for i, j, k in data) + 1,
    min(k for i, j, k in data) - 1,
    max(k for i, j, k in data) + 1,
)

# fill via BFS
queue = deque([(min_i, min_j, min_k)])
while queue:
    i, j, k = queue.popleft()
    if (i, j, k) in data:
        continue
    data.add((i, j, k))
    for ni, nj, nk in find_neighbouring_indices_3d(i, j, k):
        if (
            (ni, nj, nk) not in data
            and min_i <= ni <= max_i
            and min_j <= nj <= max_j
            and min_k <= nk <= max_k
        ):
            queue.append((ni, nj, nk))

for i, j, k in product(
    range(min_i, max_i + 1), range(min_j, max_j + 1), range(min_k, max_k + 1)
):
    if (i, j, k) not in data:
        sides_count -= len(
            [n for n in find_neighbouring_indices_3d(i, j, k) if n in data]
        )

print(sides_count)
