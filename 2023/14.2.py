import sys
from pprint import pprint
import collections

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


def rotate_grid(grid):
    grid.reverse()

    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]


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


def calculate_load(grid):
    load = 0

    multiplier = len(grid)
    for row in grid:
        rock_count = row.count("O")
        load += rock_count * multiplier
        multiplier -= 1

    return load


def display_grid(grid):
    print("\n".join(["".join(row) for row in grid]))
    print()


def get_next_grid(grid):
    for _ in range(4):
        tilt_north(grid)
        rotate_grid(grid)


def are_matrices_equal(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True


def serialize_grid(grid):
    return "|".join(["".join(row) for row in grid])


def deserialize_grid(key):
    return [list(row) for row in key.split("|")]


def spin_cycle(grid, k):
    # Graph representation of grid cycle
    cache = {}
    sequence = []

    ptr = 0
    start = -1
    while ptr < k:
        get_next_grid(grid)
        serialized = serialize_grid(grid)

        if serialized in cache:
            start = cache[serialized]
            break
        else:
            cache[serialized] = ptr
            sequence.append(serialized)

        ptr += 1

    return start, ptr, sequence


grid = parse_input()

k = 1000000000

start, end, sequence = spin_cycle(grid, k)

cycle_length = end - start
k -= start
k = k % cycle_length

print(
    "Ans: ", calculate_load(deserialize_grid(sequence[(start + k - 1) % len(sequence)]))
)
