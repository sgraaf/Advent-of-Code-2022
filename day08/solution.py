from functools import reduce
from itertools import product
from operator import mul

from aocli import find_dimensions_2d, read, to_lines

print("--- Day 8: Treetop Tree House ---")

# read the input data from `input.txt`
data = [list(map(int, list(line))) for line in to_lines(read("test_00.txt"))]

# part one
print("--- Part One ---")


def is_tallest(line_segment: list[int], tree: int) -> bool:
    return max(line_segment) == tree and line_segment.count(tree) == 1


height, width = find_dimensions_2d(data)
visible_trees = 2 * (width + height - 2)
for i, j in product(range(1, height - 1), range(1, width - 1)):
    tree = data[i][j]
    if any(
        (
            is_tallest(data[i][: j + 1], tree),  # left
            is_tallest(data[i][j:], tree),  # right
            is_tallest([row[j] for row in data[: i + 1]], tree),  # top
            is_tallest([row[j] for row in data[i:]], tree),  # bottom
        )
    ):
        visible_trees += 1
print(visible_trees)

# part two
print("--- Part Two ---")


def viewing_distance(line_segment: list[int], tree: int) -> int:
    viewing_distance = 0
    for other in line_segment:
        viewing_distance += 1
        if other >= tree:
            break
    return viewing_distance


scenic_scores = []
for i, j in product(range(1, height - 1), range(1, width - 1)):
    tree = data[i][j]
    scenic_scores.append(
        reduce(
            mul,
            (
                viewing_distance(data[i][:j][::-1], tree),  # left
                viewing_distance(data[i][j + 1 :], tree),  # right
                viewing_distance([row[j] for row in data[:i]][::-1], tree),  # top
                viewing_distance([row[j] for row in data[i + 1 :]], tree),  # bottom
            ),
        )
    )
print(max(scenic_scores))
