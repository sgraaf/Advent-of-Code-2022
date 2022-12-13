from itertools import zip_longest
from typing import Any, Optional

from aocli import read, to_lines

print("--- Day 13: Distress Signal ---")

# read the input data from `input.txt`
data = []
for packet_pair in read("input.txt").split("\n\n"):
    data.append(tuple(map(eval, to_lines(packet_pair))))


def compare(left: list[Any] | int, right: list[Any] | int) -> Optional[bool]:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left == right:
            return None
        return False

    # convert to list if one of the values is a single int
    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    for _left, _right in zip_longest(left, right, fillvalue=None):
        if _left is None:  # left ran out of items first
            return True

        if _right is None:  # right ran out of items first
            return False

        result = compare(_left, _right)
        if result is not None:
            return result


# part one
print("--- Part One ---")
right_order_idxs = []
for i, (packet_1, packet_2) in enumerate(data):
    if compare(packet_1, packet_2):
        right_order_idxs.append(i + 1)

print(sum(right_order_idxs))

# part two
print("--- Part Two ---")


def insertion_sort(data: list[Any]) -> None:
    for i, val in enumerate(data):
        for j in range(i - 1, -1, -1):
            if compare(val, data[j]):
                data[j + 1] = data[j]
                data[j] = val


# flatten packet pairs
data = [packet for packet_pair in data for packet in packet_pair]

# add divider packets
divider_packets = [[[2]], [[6]]]
data += divider_packets

# sort!
insertion_sort(data)

print((data.index(divider_packets[0]) + 1) * (data.index(divider_packets[1]) + 1))
