import collections
import sys
import time
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    pipes = []

    for line in sys.stdin:
        line = list(line.strip())
        pipes.append(line)

    return pipes


def find_start_pos(pipes):
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == "S":
                return i, j


def is_movement_possible_from_s(dx, dy, next_char):
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal

    possible_movements = {
        # West
        (0, -1): ("-", "L", "F"),
        # East
        (0, 1): ("-", "J", "7"),
        # North
        (-1, 0): ("|", "7", "F"),
        # South
        (1, 0): ("|", "L", "J"),
    }

    return next_char in possible_movements[(dx, dy)]


def display_loop(longest_loop_set, pipes):
    m, n = len(pipes), len(pipes[0])
    for i in range(m):
        print(*[pipes[i][j] if (i, j) in longest_loop_set else "." for j in range(n)])
    print()


def find_longest_loop(pipes, x, y):
    m, n = len(pipes), len(pipes[0])
    longest_loop = []
    longest_loop_length = 0

    # x, y, path, visited
    start_x, start_y = x, y
    stack = [(x, y, [], set())]
    while stack:
        x, y, curr_path, visited = stack.pop()
        if not 0 <= x < m or not 0 <= y < n or pipes[x][y] not in dir_map:
            continue

        # display_loop(set(curr_path), pipes)
        # time.sleep(0.2)
        # Update longest path
        if x == start_x and y == start_y:
            # display_loop(set(curr_path), pipes)
            if len(curr_path) > longest_loop_length:
                longest_loop_length = len(curr_path)
                longest_loop = curr_path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in dir_map[pipes[x][y]]:
            next_x = x + dx
            next_y = y + dy

            if 0 <= next_x < m and 0 <= next_y < n:
                if pipes[x][y] == "S" and not is_movement_possible_from_s(
                    dx, dy, pipes[next_x][next_y]
                ):
                    continue
                stack.append((next_x, next_y, curr_path + [(x, y)], visited))

    # print("Loop length:", len(longest_loop))

    return longest_loop, longest_loop_length


def fix_source_char(grid, sx, sy):
    # Grid contains only the longest loop
    m = len(grid)
    n = len(grid[0])

    # Key: Left, Right, Top, Bottom
    # 1 means occupied and 0 means unoccupied
    positions = {
        (1, 0, 1, 0): "J",
        (1, 1, 0, 0): "-",
        (1, 0, 0, 1): "7",
        (0, 1, 0, 1): "F",
        (0, 1, 1, 0): "L",
        (0, 0, 1, 1): "|",
    }

    left = 0
    right = 0
    top = 0
    bottom = 0

    if sy - 1 >= 0 and grid[sx][sy - 1] in ("-", "L", "F"):
        left = 1
    if sy + 1 < n and grid[sx][sy + 1] in ("-", "J", "7"):
        right = 1
    if sx - 1 >= 0 and grid[sx - 1][sy] in ("|", "7", "F"):
        top = 1
    if sx + 1 < m and grid[sx + 1][sy] in ("|", "L", "J"):
        bottom = 1

    grid[sx][sy] = positions[(left, right, top, bottom)]


def ray_cast(grid):
    m = len(grid)
    n = len(grid[0])

    # for row in grid:
    #     print(*row)

    area = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                freq = {
                    "|": 0,
                    "F": 0,
                    "J": 0,
                    "L": 0,
                    "7": 0,
                }
                for k in range(j + 1, n):
                    if grid[i][k] in freq:
                        freq[grid[i][k]] += 1

                intersections = (
                    freq["|"] + min(freq["F"], freq["J"]) + min(freq["L"], freq["7"])
                )
                if intersections % 2:
                    area += 1

    return area


def get_area_inside_loop(pipes, loop_path):
    m, n = len(pipes), len(pipes[0])
    loop_matrix = [[0] * n for _ in range(m)]
    loop_path_set = set(loop_path)

    for i in range(m):
        for j in range(n):
            if (i, j) in loop_path_set:
                loop_matrix[i][j] = pipes[i][j]

    sx, sy = find_start_pos(loop_matrix)
    fix_source_char(loop_matrix, sx, sy)

    return ray_cast(loop_matrix)


pipes = parse_input()

dir_map = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    "S": [(0, 1), (1, 0), (-1, 0), (0, -1)],
}

# Locate S
start_x, start_y = find_start_pos(pipes)

# Find the longest loop
longest_loop, longest_loop_length = find_longest_loop(pipes, start_x, start_y)

area = get_area_inside_loop(pipes, longest_loop)
print("Area: ", area)
