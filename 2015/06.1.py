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


def count_lights(grid):
    ans = 0
    for row in grid:
        ans += row.count(True)

    return ans


def solve(instructions):
    n = 1000
    grid = [[False] * n for _ in range(n)]

    for instr_type, from_coord, to_coord in instructions:
        if instr_type == 0 or instr_type == 1:
            replacement = True
            if instr_type == 1:
                replacement = False
            for i in range(from_coord[0], to_coord[0] + 1):
                for j in range(from_coord[1], to_coord[1] + 1):
                    grid[i][j] = replacement

        else:
            for i in range(from_coord[0], to_coord[0] + 1):
                for j in range(from_coord[1], to_coord[1] + 1):
                    grid[i][j] = not grid[i][j]

    return count_lights(grid)


if __name__ == "__main__":
    instructions = parse_input()
    print(solve(instructions))
