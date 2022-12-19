import functools
import re
from collections import defaultdict
from itertools import product

from aocli import Graph, read, to_lines

print("--- Day 16: Proboscidea Volcanium ---")

# read the input data from `input.txt`
graph = Graph()
for line in to_lines(read("input.txt")):
    match = re.match(r"Valve ([A-Z]{2}) has flow rate=(\d+)", line.split(";")[0])
    if match:
        valve, flow_rate = match.groups()
        graph.add_vertex(valve, int(flow_rate))
        for other_valve in re.findall(r"[A-Z]{2}", line.split(";")[1]):
            graph.add_edge(valve, other_valve, 1)

# part one
print("--- Part One ---")

# get all valves with non-zero flow rate
valves = frozenset(valve for valve, flow_rate in graph.vertices.items() if flow_rate)

# pre-compute distances between all valves
distances = defaultdict(dict)
for valve, other_valve in product(graph.vertices, graph.vertices):
    if valve != other_valve:
        distances[valve][other_valve] = graph.dijkstra(valve, other_valve)


@functools.cache
def get_max_pressure(
    time_left: int,
    valves_left: frozenset[str],
    current_valve: str = "AA",
    elephant: bool = False,
) -> list[tuple[list[str], int]]:
    return max(
        [
            graph.vertices[valve] * (time_left - distances[current_valve][valve] - 1)
            + get_max_pressure(
                time_left - distances[current_valve][valve] - 1,
                valves_left - {valve},
                valve,
                elephant,
            )
            for valve in valves_left
            if distances[current_valve][valve] < time_left
        ]
        + [get_max_pressure(26, valves_left) if elephant else 0]
    )


max_pressure = get_max_pressure(30, valves)
print(max_pressure)

# part two
print("--- Part Two ---")
max_pressure = get_max_pressure(26, valves, elephant=True)
print(max_pressure)
