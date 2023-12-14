import sys
from pprint import pprint


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    grid = []

    for line in sys.stdin:
        grid.append(list(line.strip()))

    return grid


def tilt_north(grid):
    fill_map = {0: "O", 1: ".", 2: "#"}

    for col in range(len(grid[0])):
        freq = []

        hashes = rocks = dots = 0
        for row in range(len(grid)):
            if grid[row][col] == "#":
                hashes += 1
                freq.append((rocks, dots, hashes))
                hashes = rocks = dots = 0
            elif grid[row][col] == "O":
                rocks += 1
            else:
                dots += 1
        freq.append((rocks, dots, hashes))

        row = 0
        freq_ptr = 0
        while freq_ptr < len(freq):
            # len(freq[freq_ptr]) = 3
            for i in range(3):
                for _ in range(freq[freq_ptr][i]):
                    grid[row][col] = fill_map[i]
                    row += 1
            freq_ptr += 1

    # print("\n".join(["".join(row) for row in grid]))


def calculate_load(grid):
    load = 0

    multiplier = len(grid)
    for row in grid:
        rock_count = row.count("O")
        load += rock_count * multiplier
        multiplier -= 1

    return load


grid = parse_input()
tilt_north(grid)

print("Ans: ", calculate_load(grid))
