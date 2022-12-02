from aocli import read, to_lines

print("--- Day 2: Rock Paper Scissors ---")

# read the input data from `input.txt`
data = [line.split(" ") for line in to_lines(read("input.txt"))]


def abc_to_score(a: str) -> int:
    return ord(a) - 64


def xyz_to_abc(x: str) -> str:
    return chr(ord(x) - 23)


def compute_score(a_1: str, a_2: str) -> int:
    if ord(a_2) - ord(a_1) in {1, -2}:
        return 6
    elif a_2 == a_1:
        return 3
    return 0


def wrap_abc(a: str) -> str:
    return chr(ord("A") + (ord(a) - ord("A")) % (ord("D") - ord("A")))


def abc_and_result_to_abc(a_1: str, result: str) -> str:
    if result == "X":
        a_2 = chr(ord(a_1) - 1)
    elif result == "Y":
        return a_1
    elif result == "Z":
        a_2 = chr(ord(a_1) + 1)
    return wrap_abc(a_2)


# part one
print("--- Part One ---")
score = 0
for a_1, x in data:
    a_2 = xyz_to_abc(x)
    score += abc_to_score(a_2) + compute_score(a_1, a_2)

print(score)

# part two
print("--- Part Two ---")
score = 0
for a_1, result in data:
    a_2 = abc_and_result_to_abc(a_1, result)
    score += abc_to_score(a_2) + compute_score(a_1, a_2)

print(score)
