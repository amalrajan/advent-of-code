import bisect
import heapq
import math
import os
import sys
from collections import *
from typing import *

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    instructions = []
    for line in sys.stdin:
        line = line.strip().split()
        item = []

        if line[0] == "toggle":
            # 2 for toggle
            item.append(2)
            line = line[1:]
        else:
            if line[1] == "on":
                # 0 for on
                item.append(0)
            else:
                # 1 for off
                item.append(1)
            line = line[2:]

        # Get the coordinates
        for i in (0, 2):
            item.append([int(x) for x in line[i].split(",")])

        instructions.append(item)

    return instructions


def sum_brightness(grid):
    ans = 0
    for row in grid:
        ans += sum(row)

    return ans


def solve(instructions):
    n = 1000
    grid = [[0] * n for _ in range(n)]

    score = {
        0: 1,
        1: -1,
        2: 2,
    }

    for instr_type, from_coord, to_coord in instructions:
        for i in range(from_coord[0], to_coord[0] + 1):
            for j in range(from_coord[1], to_coord[1] + 1):
                grid[i][j] = max(0, grid[i][j] + score[instr_type])

    return sum_brightness(grid)


if __name__ == "__main__":
    instructions = parse_input()
    print(solve(instructions))
