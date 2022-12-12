import re
from collections import defaultdict, deque
from copy import deepcopy
from functools import reduce
from math import lcm
from operator import mul
from typing import Any, Optional

from aocli import read, to_lines

print("--- Day 11: Monkey in the Middle ---")

# read the input data from `input.txt`
data = defaultdict(dict)
for i, monkey_data in enumerate(read("input.txt").split("\n\n")):
    for line in to_lines(monkey_data):
        line = line.strip()
        if line.startswith("Starting items:"):  # items
            data[i]["items"] = deque(map(int, re.findall(r"\d+", line)))
        elif line.startswith("Operation:"):  # operation
            data[i]["operation"] = line.removeprefix("Operation: new = ").replace(
                "old", "{old}"
            )
        elif line.startswith("Test:"):  # test
            data[i]["div_by"] = int(line.removeprefix("Test: divisible by "))
        elif line.startswith("If true:"):  # true test
            data[i]["pass_if_true"] = int(
                line.removeprefix("If true: throw to monkey ")
            )
        elif line.startswith("If false:"):  # false test
            data[i]["pass_if_false"] = int(
                line.removeprefix("If false: throw to monkey ")
            )
        data[i]["inspect_count"] = 0
_data = deepcopy(data)


def run_round(data: dict[int, dict[str, Any]], modulus: Optional[int] = None):
    for monkey_data in data.values():
        while monkey_data["items"]:
            monkey_data["inspect_count"] += 1
            worry_level = monkey_data["items"].popleft()
            worry_level = eval(monkey_data["operation"].format(old=worry_level))
            if modulus is None:
                worry_level = worry_level // 3
            else:
                worry_level = worry_level % modulus
            if worry_level % monkey_data["div_by"] == 0:
                target = monkey_data["pass_if_true"]
            else:
                target = monkey_data["pass_if_false"]
            data[target]["items"].append(worry_level)


# part one
print("--- Part One ---")
for round in range(20):
    run_round(data)

print(
    reduce(
        mul,
        sorted([monkey_data["inspect_count"] for monkey_data in data.values()])[-2:],
    )
)

# part two
print("--- Part Two ---")
data = _data
modulus = lcm(*[monkey_data["div_by"] for monkey_data in data.values()])
for round in range(10_000):
    run_round(data, modulus)

print(
    reduce(
        mul,
        sorted([monkey_data["inspect_count"] for monkey_data in data.values()])[-2:],
    )
)
