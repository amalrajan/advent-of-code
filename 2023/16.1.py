import sys

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


def simulate_beam(grid):
    m, n = len(grid), len(grid[0])

    coordinates = {"L": (0, -1), "R": (0, 1), "T": (-1, 0), "B": (1, 0)}
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
    stack = [(0, 0, 0, 1)]
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


def count_energized_tiles(grid):
    cnt = 0
    for row in grid:
        cnt += row.count("#")

    return cnt


grid = parse_input()
track = simulate_beam(grid)

print("Ans:", count_energized_tiles(track))
