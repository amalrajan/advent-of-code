import sys
import copy

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    grid = []
    for line in sys.stdin:
        grid.append(line.strip())

    return grid


def simulate_beam(grid, start_x, start_y, dx, dy):
    m, n = len(grid), len(grid[0])

    coordinates = {"L": (0, -1), "R": (0, 1), "T": (-1, 0), "B": (1, 0)}

    # This reads as:
    # If the beam is coming from (x, y) where (x, y) is the key
    # It can reflect in any of the direction_map[(x, y)] directions
    direction_map = {
        (0, -1): {
            "-": ("L"),
            "|": ("B", "T"),
            "/": ("B"),
            "\\": ("T"),
            ".": ("L"),
        },
        (0, 1): {
            "-": ("R"),
            "|": ("B", "T"),
            "/": ("T"),
            "\\": ("B"),
            ".": ("R"),
        },
        (-1, 0): {
            "-": ("L", "R"),
            "|": ("T"),
            "/": ("R"),
            "\\": ("L"),
            ".": ("T"),
        },
        (1, 0): {
            "-": ("L", "R"),
            "|": ("B"),
            "/": ("L"),
            "\\": ("R"),
            ".": ("B"),
        },
    }

    track = [["." for _ in range(n)] for __ in range(m)]

    # x, y, dx, dy
    # Stack because it is memory efficient.
    stack = [(start_x, start_y, dx, dy)]

    visited = set()

    while stack:
        key = stack.pop()
        x, y, dx, dy = key

        if key in visited:
            continue
        visited.add(key)
        track[x][y] = "#"

        curr = grid[x][y]
        for ch in direction_map[(dx, dy)][curr]:
            ndx, ndy = coordinates[ch]
            if 0 <= x + ndx < m and 0 <= y + ndy < n:
                stack.append((x + ndx, y + ndy, ndx, ndy))

    return track


def find_max_energized_tiles(grid):
    max_energized_tiles = 0

    # Check for leftmost and rightmost column
    for i in range(len(grid)):
        max_energized_tiles = max(
            max_energized_tiles,
            count_energized_tiles(simulate_beam(grid, i, 0, 0, 1)),
            count_energized_tiles(simulate_beam(grid, i, len(grid[0]) - 1, 0, -1)),
        )

    # Check for top and bottom rows
    for j in range(len(grid[0])):
        max_energized_tiles = max(
            max_energized_tiles,
            count_energized_tiles(simulate_beam(grid, 0, j, 1, 0)),
            count_energized_tiles(simulate_beam(grid, len(grid) - 1, j, -1, 0)),
        )

    return max_energized_tiles


def count_energized_tiles(grid):
    cnt = 0
    for row in grid:
        cnt += row.count("#")

    return cnt


grid = parse_input()

print("Ans:", find_max_energized_tiles(grid))
