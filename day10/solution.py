from aocli import read, to_lines

print("--- Day 10: Cathode-Ray Tube ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# part one
print("--- Part One ---")
X = 1
current_instruction = None
current_increase = 0
signal_strengths = []
crt = ""
for cycle in range(1, 241):
    crt += "#" if (X - 1) <= ((cycle - 1) % 40) <= (X + 1) else "."
    if (cycle - 20) % 40 == 0:
        signal_strengths.append(cycle * X)
    if cycle % 40 == 0:
        crt += "\n"

    if current_instruction is None:
        # get the next instruction
        current_instruction = data.pop(0)

        if current_instruction == "noop":
            current_instruction = None
            continue

        if current_instruction.startswith("addx"):
            current_increase = int(current_instruction.split(" ")[1])
    else:
        # increase the register
        X += current_increase
        current_instruction = None

print(sum(signal_strengths))

# part two
print("--- Part Two ---")
print(crt)
