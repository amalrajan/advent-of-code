import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    crates = []
    instructions = []

    stack_count = 0
    for line in sys.stdin:
        if line.isspace():
            break
        layer = ()
        for i in range(0, len(line), 4):
            layer += (line[i : i + 4].strip()[1:-1],)
        crates.append(tuple(layer))
        stack_count = max(stack_count, len(layer))
    crates = crates[:-1]

    stacks = [[] for _ in range(stack_count)]

    for i in range(len(crates)):
        for j in range(len(crates[i])):
            if crates[i][j]:
                stacks[j].append(crates[i][j])

    for i in range(len(stacks)):
        stacks[i].reverse()

    for line in sys.stdin:
        line = line.strip().split()
        # Move [1] crates from [3] -> [5]
        instructions.append((int(line[3]) - 1, int(line[5]) - 1, int(line[1])))

    return stacks, instructions


def simulate_instructions(stacks, instructions):
    for source, dest, crate_count in instructions:
        for _ in range(crate_count):
            stacks[dest].append(stacks[source].pop())

    return "".join(stack[-1] if stack else "" for stack in stacks)


stacks, instructions = parse_input()

res = simulate_instructions(stacks, instructions)
print(res)
