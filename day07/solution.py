from __future__ import annotations

import re

from aocli import read, to_lines

print("--- Day 7: No Space Left On Device ---")


class Tree:
    def __init__(self, name: str, size: int | None = None):
        self.parent = None
        self.children: list[Tree] = []
        self.name = name
        self.size = size

    def add_child(self, child: Tree) -> None:
        child.parent = self
        self.children.append(child)

    def __getitem__(self, name: str) -> Tree:
        for child in self.children:
            if child.name == name:
                return child
        raise KeyError(f"Child {name} not found in {self}")

    @property
    def all_children(self) -> list[Tree]:
        return self.children + [
            c for child in self.children for c in child.all_children
        ]

    @property
    def total_size(self) -> int:
        return sum(node.size for node in self.all_children if node.size is not None)

    def __repr__(self) -> str:
        return f"Tree('{self.name}', {self.size}, {self.children})"


# read the input data from `input.txt`
data = to_lines(read("input.txt"))

root_node = None
current_node = None
for line in data:
    if line.startswith("$"):  # command
        if line.startswith("$ cd "):
            new_directory = line.removeprefix("$ cd ")
            if new_directory == "..":
                if current_node is not None:
                    current_node = current_node.parent
            else:
                if current_node is None:
                    root_node = Tree(new_directory)
                    current_node = root_node
                else:
                    current_node = current_node[new_directory]
    elif (m := re.match(r"dir (\w+)", line)) is not None:  # directory
        new_node = Tree(m.group(1))
        if current_node is not None:
            current_node.add_child(new_node)
    elif (m := re.match(r"(\d+) (.*)", line)) is not None:  # file
        new_node = Tree(m.group(2), int(m.group(1)))
        if current_node is not None:
            current_node.add_child(new_node)

# part one
print("--- Part One ---")
total_sizes_sum = 0
for node in root_node.all_children:
    if node.size is None:
        if node.total_size <= 100_000:
            total_sizes_sum += node.total_size
print(total_sizes_sum)

# part two
print("--- Part Two ---")
thresh = 30_000_000 - (70_000_000 - root_node.total_size)
deletion_candidates = []
for node in [root_node] + root_node.all_children:
    if node.size is None:
        if node.total_size >= thresh:
            deletion_candidates.append(node)

print(min(deletion_candidates, key=lambda node: node.total_size).total_size)
