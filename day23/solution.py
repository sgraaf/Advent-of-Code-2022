from collections import defaultdict
from itertools import count, product
from typing import Iterable

from aocli import find_neighbouring_indices_2d, read, to_lines

print("--- Day 23: Unstable Diffusion ---")

# read the input data from `input.txt`
data = defaultdict(lambda: ".")
for i, line in enumerate(to_lines(read("input.txt"))):
    for j, c in enumerate(line):
        data[(i, j)] = c


def filter_coordinates(
    coordinates: Iterable[tuple[int, int]], filter: str = "#"
) -> list[tuple[int, int]]:
    return [c for c in coordinates if data[c] == filter]


def get_bounds(grid: dict[tuple[int, int], str]) -> tuple[int, int, int, int]:
    return (
        min(i for (i, j), val in grid.items() if val == "#"),
        max(i for (i, j), val in grid.items() if val == "#"),
        min(j for (i, j), val in grid.items() if val == "#"),
        max(j for (i, j), val in grid.items() if val == "#"),
    )


def run_round(
    grid: dict[tuple[int, int], str],
    directions_map: dict[tuple[tuple[int, int], ...], tuple[int, int]],
) -> bool:
    proposals = defaultdict(list)
    for (i, j) in filter_coordinates(grid.keys()):
        neighbors = filter_coordinates(
            find_neighbouring_indices_2d(i, j, include_diagonals=True)
        )
        if neighbors:
            for directions, (pi, pj) in directions_map.items():
                if all([grid[(i + di, j + dj)] == "." for di, dj in directions]):
                    proposals[(i + pi, j + pj)].append((i, j))
                    break

    if not proposals:
        return True

    # move
    for (pi, pj), elves in proposals.items():
        if len(elves) == 1:
            grid[elves[0]] = "."

    for (pi, pj), elves in proposals.items():
        if len(elves) == 1:
            grid[(pi, pj)] = "#"

    # update directions
    direction = next(iter(directions_map))
    directions_map[direction] = directions_map.pop(direction)

    return False


# part one
print("--- Part One ---")
rounds = 10
directions_map = {
    ((-1, -1), (-1, 0), (-1, 1)): (-1, 0),  # N
    ((1, -1), (1, 0), (1, 1)): (1, 0),  # S
    ((-1, -1), (0, -1), (1, -1)): (0, -1),  # W
    ((-1, 1), (0, 1), (1, 1)): (0, 1),  # E
}
for round in range(rounds):
    if run_round(data, directions_map):
        break


min_i, max_i, min_j, max_j = get_bounds(data)
print(
    len(
        filter_coordinates(
            product(range(min_i, max_i + 1), range(min_j, max_j + 1)), "."
        )
    )
)

print("--- Part Two ---")
for round in count(rounds + 1):
    if run_round(data, directions_map):
        break

print(round)
