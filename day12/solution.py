from aocli import (
    Graph,
    find_dimensions_2d,
    find_neighbouring_indices_2d,
    read,
    to_lines,
)

print("--- Day 12: Hill Climbing Algorithm ---")

# read the input data from `input.txt`
data = [list(line) for line in to_lines(read("input.txt"))]
height, width = find_dimensions_2d(data)

g = Graph()
start = end = -1, -1
possible_starts = []
for i, row in enumerate(data):
    for j, val in enumerate(row):
        if val == "S":  # start
            start = i, j
            val = "a"
        elif val == "E":  # end
            end = i, j
            val = "z"

        if val == "a":  # possible starts
            possible_starts.append((i, j))

        neighbors = find_neighbouring_indices_2d(i, j, (0, height), (0, width))
        for _i, _j in neighbors:
            _val = data[_i][_j]
            if ord(_val) <= ord(val) + 1:
                g.add_edge((i, j), (_i, _j), 1)

# part one
print("--- Part One ---")
print(g.dijkstra(start, end))


# part two
print("--- Part Two ---")
print(min(g.dijkstra(start, end) for start in possible_starts))
