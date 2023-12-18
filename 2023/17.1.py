import collections
import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    # sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


# This code (BFS / DFS) does not
# work as it is too slow

def parse_input():
    grid = []
    for line in sys.stdin:
        grid.append([int(x) for x in line.strip()])

    return grid


def display(grid, ppath):
    m, n = len(grid), len(grid[0])
    path_grid = [["." for _ in range(n)] for __ in range(m)]
    itr = 1
    for x, y in ppath:
        path_grid[x][y] = itr
        itr += 1
    for i in range(len(path_grid)):
        for j in range(len(path_grid[0])):
            if path_grid[i][j] != ".":
                print(str(path_grid[i][j]).ljust(3), end="")
            else:
                print(".".ljust(3), end="")

        print()


def traverse(grid):
    m = len(grid)
    n = len(grid[0])

    queue = collections.deque([(0, 0, 0, 1, 0, 1, set(), [])])
    dest = (m - 1, n - 1)
    min_heat_loss = math.inf

    while queue:
        x, y, dx, dy, heat_loss, steps, visited, ppath = queue.popleft()
        if not 0 <= x < m or not 0 <= y < n:
            continue

        if (x, y) in visited:
            continue

        if (x, y) == dest:
            ppath += [(x, y)]

            if heat_loss + grid[x][y] < min_heat_loss:
                min_heat_loss = min(min_heat_loss, heat_loss + grid[x][y])
                continue

        visited.add((x, y))

        if steps % 3 == 0:
            for possible_steps in range(1, 3):
                # Traverse 90 left
                ndx, ndy = -dy, dx
                queue.append(
                    (
                        x + ndx,
                        y + ndy,
                        ndx,
                        ndy,
                        heat_loss + grid[x][y],
                        possible_steps,
                        visited.copy(),
                        ppath + [(x, y)],
                    )
                )
                # Traverse 90 right
                ndx, ndy = dy, -dx
                queue.append(
                    (
                        x + ndx,
                        y + ndy,
                        ndx,
                        ndy,
                        heat_loss + grid[x][y],
                        possible_steps,
                        visited.copy(),
                        ppath + [(x, y)],
                    )
                )
        else:
            queue.append(
                (
                    x + dx,
                    y + dy,
                    dx,
                    dy,
                    heat_loss + grid[x][y],
                    1 + steps,
                    visited.copy(),
                    ppath + [(x, y)],
                )
            )

    return min_heat_loss


grid = parse_input()
for row in grid:
    print(row)

print(traverse(grid))
