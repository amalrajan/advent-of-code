import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        line = line.strip().split()
        line = [x.rstrip(",") for x in line]
        inputs.append(line)

    return inputs


def solve(instructions):
    variables = collections.defaultdict(int)

    idx = 0
    while idx < len(instructions):
        inst = instructions[idx]

        if inst[0] == "inc":
            variables[inst[1]] += 1
            idx += 1
        elif inst[0] == "hlf":
            variables[inst[1]] //= 2
            idx += 1
        elif inst[0] == "tpl":
            variables[inst[1]] *= 3
            idx += 1
        elif inst[0] == "jmp":
            offset = int(inst[1])
            idx += offset
        elif inst[0] == "jie":
            variable, offset = inst[1], int(inst[2])
            if variables[variable] % 2 == 0:
                idx += offset
            else:
                idx += 1
        elif inst[0] == "jio":
            variable, offset = inst[1], int(inst[2])
            if variables[variable] == 1:
                idx += offset
            else:
                idx += 1

    return variables["b"]


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
