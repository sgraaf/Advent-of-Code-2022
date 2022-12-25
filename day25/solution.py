from aocli import read, to_lines

print("--- Day 25: Full of Hot Air ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))


def snafu_to_decimal(snafu: str) -> int:
    d = 0
    for i, c in enumerate(reversed(snafu)):
        if c == "-":
            c = "-1"
        if c == "=":
            c = "-2"
        d += int(c) * 5**i
    return d


def decimal_to_snafu(d: int) -> str:
    snafu = []
    while d > 0:
        c = int(d % 5)
        snafu.append(c)
        d //= 5

    # add leading zero
    snafu += [0]

    # reverse it
    snafu = snafu[::-1]

    for i in range(len(snafu) - 1, -1, -1):
        c = snafu[i]
        if c == 3:
            snafu[i] = "="
            snafu[i - 1] += 1
        elif c == 4:
            snafu[i] = "-"
            snafu[i - 1] += 1
        elif c == 5:
            snafu[i] = "0"
            snafu[i - 1] += 1
        else:
            snafu[i] = str(c)

    return "".join(snafu).removeprefix("0")


# part one
print("--- Part One ---")

print(decimal_to_snafu(sum(snafu_to_decimal(snafu) for snafu in data)))
