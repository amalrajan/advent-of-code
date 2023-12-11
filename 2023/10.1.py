import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


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


def find_longest_loop(pipes, x, y):
    m, n = len(pipes), len(pipes[0])
    # longest_loop = []
    longest_loop_length = 0

    # x, y, path, visited
    stack = [(x, y, [], set())]
    start_x, start_y = x, y
    while stack:
        x, y, curr_path, visited = stack.pop()
        if not 0 <= x < m or not 0 <= y < n or pipes[x][y] not in dir_map:
            continue

        # Update longest path
        if x == start_x and y == start_y and len(curr_path) > longest_loop_length:
            longest_loop_length = len(curr_path)
            # longest_loop = curr_path

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
    # for x, y in longest_loop:
    #     print(pipes[x][y], end=" ")
    # print()

    return longest_loop_length


pipes = []
for line in sys.stdin:
    line = list(line.strip())
    pipes.append(line)

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
longest_loop_length = find_longest_loop(pipes, start_x, start_y)

print("Ans: ", longest_loop_length // 2)
